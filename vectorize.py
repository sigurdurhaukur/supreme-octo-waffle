import weaviate
from data_processing import process_text
import json

# Create a client for your Weaviate instance
client = weaviate.Client("http://localhost:8080")

# client.schema.delete_class("News")

# class_obj = {
#     "class": "News",
#     "description": "News articles",
#     "vectorizer": "text2vec-transformers",
# }

# client.schema.create_class(class_obj)

# # import data
# data = [{"title": "Seg­ir dótt­ur sína og þrjú barna­börn á meðal lát­inna ", "url": "https://www.mbl.is/frettir/erlent/2023/05/02/segir_dottur_sina_og_thrju_barnaborn_a_medal_latinn/"},
#         {"title": "Líf Þorsteins hefur alla tíð snúist um sjóinn og fiskveiðar. Á fertugsaldri uppgötvaði hann svo",
#             "url": "https://mbl.is/"},
#         {"title": "Þurfti að slaka á og fór á fullt í hjól­reiðar ",
#             "url": "https://www.mbl.is/frettir/innlent/2023/05/02/thurfti_ad_slaka_a_og_for_a_fullt_i_hjolreidar/"},
#         {"title": "Til stóð að gera upp þennan gamla Land Rover sem stóð í húsakynnum vélsmiðjunnar Verma. ",
#         "url": "https://mbl.is/"},
#         {"title": "Starf­semi í hús­inu og mikið tjón ",
#          "url": "https://www.mbl.is/frettir/innlent/2023/05/02/starfsemi_i_husinu_og_mikid_tjon/"},
#         {"title": "Elliði Vignisson, bæjarstjóri Ölfuss, og Karl Wernerson, stofnandi Kamba, handssala byggingarstaðinn og fyrirhugað útlit verskmiðjunnar. ", "url": "https://mbl.is/"},
#         {"title": "Karl Werners­son bygg­ir verk­smiðju í Þor­láks­höfn ", "url": "https://www.mbl.is/vidskipti/frettir/2023/05/02/karl_wernersson_byggir_verksmidju_i_thorlakshofn/"}]


# # Configure a batch process
# with client.batch as batch:
#     batch.batch_size = 1  # 100
#     for i, d in enumerate(data):
#         try:
#             properties = {
#                 "text": d['title'],
#                 "url": d['url']
#             }

#             client.batch.add_data_object(
#                 properties, "News")
#         except Exception as e:
#             # print(e)
#             print("an error occured! most likely beacause the text could not been processed. sometimes out of vocabulary words can cause this.")
#             pass


# all_objects = client.data_object.get()
# print(json.dumps(some_objects))

# search for query
query = "fiskur afli sjór"
custom_embedding = process_text(query)

result = (
    client.query
    .get("News", ["text", 'url'])
    .with_near_text({"concepts": ["fiskur"]})
    # .with_limit(2)
    .with_additional(['certainty'])
    .do()
)

print(f"query: {query}")

# print(result)
# print("result:")
for i in result['data']['Get']['News']:
    print(i['text'])
#     print(i['_additional']['certainty'], i['text'], '\n')
# print(i['_additional']['certainty'], i['text'], i['url'], '\n')
