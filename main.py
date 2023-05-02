import weaviate
from data_processing import process_text
import json
# Create a client for your Weaviate instance
client = weaviate.Client("http://localhost:8080")

client.schema.delete_class("News")

class_obj = {
    "class": "News",
    "description": "News articles",
    "vectorizer": "none",
}

client.schema.create_class(class_obj)

# import data
data = ["Auðvelt er að lofa, örðugt að efna", "mamma", "afi", "pabbi"]


# Configure a batch process
with client.batch as batch:
    batch.batch_size = 1
    for i, d in enumerate(data):
        properties = {
            "text": d,
        }
        # process the text
        sentence_vector = process_text(d)

        client.batch.add_data_object(
            properties, "News", vector=sentence_vector)


some_objects = client.data_object.get()
# print(json.dumps(some_objects))

query = "amma"
custom_embedding = process_text(query)

result = (
    client.query
    .get("News", ["text"])
    .with_near_vector({
        "vector": custom_embedding,
        # "certainty": 0.7
    })
    # .with_limit(2)
    .with_additional(['certainty'])
    .do()
)

print(f"query: {query}")

print("result:", result)
for i in result['data']['Get']['News']:
    print(i['_additional']['certainty'], i['text'])
