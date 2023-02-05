from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()

origins = [
    "http://127.0.0.1:8000/",
    "http://localhost:8000",
    "localhost:8000",
    "http://127.0.0.1:3000/",
    "http://localhost:3000",
    "localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins
)

@app.get("/")
async def root():
    return {"message": "This is the backend in Python"}

if __name__ == "__main__":
    uvicorn.run("app.api:app", host="0.0.0.0", port=8000, reload=True)