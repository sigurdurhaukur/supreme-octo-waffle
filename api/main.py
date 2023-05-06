from fastapi import FastAPI, Request, Response, status
from data_processing import vectorize

app = FastAPI()


@app.get("/")
async def root():
    return Response(status_code=200)


@app.get("/.well-known/live", response_class=Response)
@app.get("/.well-known/ready", response_class=Response)
def live_and_ready(response: Response):
    response.status_code = status.HTTP_204_NO_CONTENT


@app.get("/meta")
async def meta():
    return {"name": "word-embeddings", "language": "icelandic"}


@app.post("/vectors")
async def read_item(request: Request, response: Response):
    try:
        data = await request.json()
        text = data["text"]
        vector = await vectorize(text)
        vector = vector[0]
        print(vector.shape, vector[:5])
        return {"text": text, "vector": vector.tolist(), "dim": len(vector)}
        # return {"text": text, "vector": vector.tolist(), "dim": vector.shape[-1]}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": str(e)}
