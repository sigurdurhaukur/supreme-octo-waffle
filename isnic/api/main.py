from fastapi import FastAPI, Request, Response, status
from gensim.models import keyedvectors

word2vec = keyedvectors.KeyedVectors.load("./word2vec/word2vec.kv")

app = FastAPI(
    title="ISNIC API",
    description="API for ISNIC",
    version="0.0.1",
    docs_url="/",
    redoc_url=None,
)


@app.get("/")
async def root():
    return Response(status_code=200)


@app.get("/word2vec/{word}")
async def get_word2vec(word: str):
    try:
        return word2vec[word].tolist()
    except:
        return Response(status_code=404)


@app.get("/search/{word}")
async def search(word: str):
    word = word.split(" ")
    average_vector = None
    word_count = 0

    for w in word:
        try:
            if average_vector is None:
                average_vector = word2vec[w].copy()  # Create a copy of the vector
            else:
                average_vector += word2vec[w]
            word_count += 1
        except:
            pass

    if average_vector is not None:
        average_vector /= word_count

        try:
            topn = 10
            result = word2vec.similar_by_vector(average_vector, topn=topn)
            return result
        except:
            return Response(status_code=404)
    else:
        return Response(status_code=404)
