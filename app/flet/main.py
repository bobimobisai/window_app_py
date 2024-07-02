import flet
from src.router import MyApp
from fastapi import FastAPI
import uvicorn

app = MyApp()
flet_app = flet.app(
    target=app, host="localhost", port=8899, view=flet.WEB_BROWSER, export_asgi_app=True
)

fastapi_app = FastAPI()
fastapi_app.mount("/", flet_app)

if __name__ == "__main__":
    uvicorn.run(fastapi_app, host="localhost", port=9988)
