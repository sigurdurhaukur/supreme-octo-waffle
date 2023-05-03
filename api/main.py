from fastapi import FastAPI
from fastapi.responses import Response

app = FastAPI()


@app.get("/")
async def root():
    return Response(status_code=200)


@app.get("/.well-known/live")
async def live():
    return Response(status_code=204)


@app.get("/.well-known/ready")
async def ready():
    return Response(status_code=204)


@app.get("/meta")
async def meta():
    return {"meta": "infiramtion"}


@app.post("/vectors")
async def vectors():
    return {"text": [0.1, 0.2, 0.3, 0.4, 0.5]}
