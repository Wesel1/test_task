import asyncio

from fastapi import FastAPI

app = FastAPI()

@app.get("/calculate")
def calculate_deadlines():
    return("Hello")
