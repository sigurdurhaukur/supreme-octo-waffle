import weaviate
import wikipediaapi  # for fetching random wikipedia articles
import requests
from isl_wiki import get_wikipedia_articles as get_isl_wiki_articles  # custom module
import time
from tabulate import tabulate


def initialize_schema(client):
    """
    Initializes the schema of the weaviate instance
    It will begin by deleting all classes and then creating a new one
    """
    client.schema.delete_all()

    class_obj = {
        "class": "Articles",
        "description": "Icelandic wikipedia articles",
        "vectorizer": "text2vec-transformers",
        "properties": [
            {
                "dataType": ["string"],
                "description": "Title of the article",
                "name": "title",
                "moduleConfig": {"text2vec-transformers": {"skip": True}},
            },
            {
                "dataType": ["string"],
                "description": "url to the article",
                "name": "url",
                "moduleConfig": {"text2vec-transformers": {"skip": True}},
            },
            {
                "dataType": ["text"],
                "description": "short summary of the article",
                "name": "summary",
            },
            {
                "dataType": ["text[]"],
                "description": "list of links in the article",
                "moduleConfig": {"text2vec-transformers": {"skip": True}},
                "name": "links",
            },
        ],
    }

    client.schema.create_class(class_obj)


def add_data(client, data):
    # import data

    # Configure a batch process
    with client.batch as batch:
        batch.batch_size = 100  # 100
        for i, d in enumerate(data):
            try:
                properties = {
                    "text": d.title,
                    "url": d.url,
                    "summary": d.summary,
                    "links": d.links,
                }

                client.batch.add_data_object(properties, "Articles")
            except Exception as e:
                # print(e)
                print(
                    "an error occured! most likely beacause the text could not been processed. sometimes out of vocabulary words can cause this."
                )
                pass


def get_data(wiki_wiki):
    """gets random articles  from wikipedia"""

    response = requests.get("https://is.wikipedia.org/api/rest_v1/page/random/title")
    if response.status_code == 200:
        data = response.json()
        title = data["items"][0]["title"]
        page = wiki_wiki.page(title)

    else:
        print("Error: Could not fetch random page title")

    return {
        "title": page.title,
        "summary": page.summary,
        "url": page.fullurl,
    }


def search(client, query):
    """
    Semantic search using weaviate client
    input: query string
    output: the result and time it took to search
    """
    start_time = time.time()

    result = (
        client.query.get("Articles", ["text", "url", "summary"])
        .with_near_text({"concepts": [query]})
        # .with_limit(2) # limit the amount of results
        .with_additional(["certainty"])
        .do()
    )

    print(f"query: {query}")

    print("result:")
    for i in result["data"]["Get"]["Articles"]:
        print(i["_additional"]["certainty"], i["text"], "\n")

    return result, time.time() - start_time


def lexical_search(client, query, data):
    """
    input: Article object, with title, summary, url, links
    output: time it took to search
    """
    start_time = time.time()

    result = []
    for i in data:
        if query in i.summary:
            print(i.title)
            result.append(i)

    print(f"query: {query}")

    return result, time.time() - start_time


def measure_search_speed(client, data):
    """
    measures the search speed of the semantic search in comparison to a linear search
    """

    random_queries = [
        "Frakkland",
        "Alþingi",
        "þingmannatal",
        "mamma",
        "pabbi",
        "fiskur",
        "hundur",
        "Ólafur Ragnar Grímsson",
        "Björk",
        "Hafþór Júlíus Björnsson",
        "Pleasantville er bandarísk kvikmynd frá árinu 1998. Hún fjallar um tvíburasystkin, leikin af Tobey Maguire og Reese Witherspoon, sem sogast inn í sjónvarpsþátt.",
    ]

    lexical_speeds = []
    semantic_speeds = []
    for query in random_queries:
        _, lexical_speed = lexical_search(client, query, data)
        _, semantic_speed = search(client, query)

        lexical_speeds.append(lexical_speed)
        semantic_speeds.append(semantic_speed)

    # table of results
    print("query\tlexical\tsemantic")
    for i in range(len(random_queries)):
        print(f"{random_queries[i]}\t{lexical_speeds[i]}\t{semantic_speeds[i]}\t")

    lexical_speed = sum(lexical_speeds) / len(lexical_speeds)
    semantic_speed = sum(semantic_speeds) / len(semantic_speeds)

    print(f"lexical search speed: {lexical_speed}")
    print(f"semantic search speed: {semantic_speed}")


def check_for_common_items_in_lists(list1, list2):
    """
    checks for common items in two lists
    """

    common_items = []
    for i in list1:
        if i in list2:
            common_items.append(i)

    return len(common_items), common_items


def measure_relevance(client, data):
    percentage_amount = 0.1
    queries = [data[i].title for i in range(int(len(data) * percentage_amount))]
    print(f"measuring relevance for {len(queries)} articles")
    print("example queries: ", queries[:5])

    table = [
        ["query", "ground truth", "semantic search", "common articles", "common links"]
    ]

    for query in queries:
        try:
            ground_truth = []
            semantic_results = []

            ground_truth_links = []
            semantic_results_links = []
            # linear search
            for i in data:
                query = query.lower()
                if query in i.summary:
                    ground_truth.append(i.title.lower())
                    ground_truth_links += i.links

            # semantic search
            result = (
                client.query.get("Articles", ["text links"])
                .with_near_text({"concepts": [query]})
                .with_limit(10)
                .do()
            )

            print("semantic search results: ", result)

            semantic_results.append(
                [i["text"] for i in result["data"]["Get"]["Articles"]]
            )
            semantic_results_links += [
                i["links"] for i in result["data"]["Get"]["Articles"]
            ]

            semantic_results = semantic_results[0]
            semantic_results_links = semantic_results_links[0]

            common_items_amount, _ = check_for_common_items_in_lists(
                ground_truth, semantic_results
            )

            common_links_amount, _ = check_for_common_items_in_lists(
                ground_truth_links, semantic_results_links
            )

            table.append(
                [
                    query,
                    len(ground_truth),
                    len(semantic_results),
                    common_items_amount,
                    common_links_amount,
                ]
            )
        except Exception as e:
            print(e)
            pass

    print()
    print(tabulate(table, headers="firstrow"))


if __name__ == "__main__":
    # Create a client for your Weaviate instance
    client = weaviate.Client("http://localhost:8080")
    initialize_schema(client)

    data = get_isl_wiki_articles(max_articles=1e10)  # all articles
    # data = get_isl_wiki_articles(max_articles=100)  # for testing

    print(f"Found {len(data)} articles")
    print("adding data to weaviate")
    add_data(client, data)

    print("measuring search relevance")
    measure_relevance(client, data)

    # example search
    search(
        client,
        "þekktur fyrir viðskiptaumsvif sín og stuðning sinn við ýmsa pólitíska málstaði. Moon var stofnandi og andlegur leiðtogi Sameiningarkirkjunnar, kristins söfnuðar sem gekk út á þá trúarkenningu að Moon sjálfur væri nýr Messías sem hefði verið falið að ljúka hjálpræðisverkinu sem Jesú mistókst að vinna fyrir 2000 árum. Fylgismenn Moons eru gjarnan kallaðir „Moonistar“ ",
    )

    print("\n")

    print("measuring search speed")
    measure_search_speed(client, data)
