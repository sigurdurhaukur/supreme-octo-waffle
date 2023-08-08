import weaviate
import wikipediaapi
import json
import requests
from isl_wiki import get_wikipedia_articles as get_isl_wiki_articles
import time


def initialize_schema(client):
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
    """gets data from wikipedia"""

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
    start_time = time.time()

    result = (
        client.query.get("Articles", ["text", "url", "summary"])
        .with_near_text({"concepts": [query]})
        # .with_limit(2)
        .with_additional(["certainty"])
        .do()
    )

    print(f"query: {query}")

    # print(result)
    print("result:")
    for i in result["data"]["Get"]["Articles"]:
        # print(i["text"])
        # print(i)
        print(i["_additional"]["certainty"], i["text"], "\n")
        # print(i['_additional']['certainty'], i['text'], i['url'], '\n')

    return time.time() - start_time


def lexical_search(client, query, data):
    "input: Article object, with title, summary, url, links"
    start_time = time.time()

    for i in data:
        if query in i.summary:
            print(i.title)

    print(f"query: {query}")

    return time.time() - start_time


def measure_search_speed(client, data):
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
        lexical_speed = lexical_search(client, query, data)
        semantic_speed = search(client, query)

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


if __name__ == "__main__":
    # Create a client for your Weaviate instance
    client = weaviate.Client("http://localhost:8080")
    # initialize_schema(client)

    data = get_isl_wiki_articles(max_articles=1e10)  # all articles
    # data = get_isl_wiki_articles(max_articles=10)  # for testing

    # print(f"Found {len(data)} articles")
    # print("adding data to weaviate")
    # add_data(client, data)

    # wiki_wiki = wikipediaapi.Wikipedia("is")
    # max_pages = 2000
    # data = []
    # for i in range(max_pages):
    #     print(f"getting page {i}")
    #     new_page = get_data(wiki_wiki)
    #     if new_page["title"] not in [page["title"] for page in data]:
    #         data.append(new_page)
    #     else:
    #         print(f"Skipping page {i} with duplicate title: {new_page['title']}")

    # print(f"Fetched {len(data)} unique pages")

    # print(data)
    # # get_data(client)
    # search(
    #     client,
    #     "þekktur fyrir viðskiptaumsvif sín og stuðning sinn við ýmsa pólitíska málstaði. Moon var stofnandi og andlegur leiðtogi Sameiningarkirkjunnar, kristins söfnuðar sem gekk út á þá trúarkenningu að Moon sjálfur væri nýr Messías sem hefði verið falið að ljúka hjálpræðisverkinu sem Jesú mistókst að vinna fyrir 2000 árum. Fylgismenn Moons eru gjarnan kallaðir „Moonistar“ ",
    # )

    # print("\n")

    measure_search_speed(client, data)
