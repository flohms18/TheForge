from fastapi import FastAPI
from routers import posts



app = FastAPI()

app.frontend("/", directory="frontend/dist")

app.include_router(posts.router)


