# supreme-octo-waffle K-nn and FAISS

## Todo

- download the icelandic wiki, for actual real applications of search [10gb](https://dumps.wikimedia.org/other/static_html_dumps/current/is/)
- impliment a pipeline to put it into the vector database

## General

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

testing the api locally

```bash
uvicorn api.main:app --reload
curl -X POST -H "Content-Type: application/json" -d '{"text": "mamma"}' http://localhost:9000/vectors
```

database engine, weaviate. https://www.semi.technology/developers/weaviate/current/get-started/installation.html

## Quick start

open docker desktop and make sure it is running

to start the docker container (it contains the database)

```bash
docker-compose up -d
```

to start the front end

```bash
cd octo-waffle
npm run dev
```

## some important things

- the database is running on port 8080
- the front end is running on port 3000
- the api is running on port 9000
- to add data or to manage the database see `./vectorize.py`
