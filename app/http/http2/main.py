from fastapi import FastAPI
from httpx import AsyncClient, Timeout
from contextlib import asynccontextmanager


timeout = Timeout(10.0, connect=5.0)

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.http_client = AsyncClient(http2=True, timeout=timeout)
    yield
    await app.state.http_client.aclose()


app = FastAPI(lifespan=lifespan)


@app.get("/data")
async def get_data():
    response = await app.state.http_client.get(
        "https://jsonplaceholder.typicode.com/todos/1"
    )
    return response.json()
