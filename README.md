# supreme-octo-waffle K-nn and FAISS

Uses word2vec embeddings and faiss to find the kth nearest neighbors of a given word. The embeddings can be found here https://clarin.is/. They were created by Friðriksdóttir, Steinunn Rut ; Daníelsson, Hjalti and Steingrímsson, Steinþór.

dependencies:

```bash
pip install gensim
pip install faiss-cpu
```

download data

```bash
 curl --remote-name-all https://repository.clarin.is/repository/xmlui/bitstream/handle/20.500.12537/209{/word2vec_models.zip}

 unzip -j /work/word2vec_models.zip "IGC_2021_lemmatized__350__13__9__5__0_05__1_vectors.kv" "READ.ME"
```

api reference: https://github.com/laura-ham/t2v-spacy-models/

to build the api image

```bash
 docker-compose build api
```

database engine, weaviate. https://www.semi.technology/developers/weaviate/current/get-started/installation.html

to start the docker container (it contains the database)

```bash
docker-compose up -d
```
