from fastapi import FastAPI, Request, Response
from .data_processing import vectorize

app = FastAPI()


@ app.get("/")
async def root():
    return Response(status_code=200)


@ app.get("/.well-known/live")
async def live():
    return Response(status_code=204)


@ app.get("/.well-known/ready")
async def ready():
    return Response(status_code=204)


@ app.get("/meta")
async def meta():
    return {"meta": "infiramtion"}


@app.post("/vectors")
async def vectors(request: Request):
    data = await request.json()
    text = data["text"]
    vectors = vectorize(text).tolist()
    return {"text": text, "vectors": vectors}
