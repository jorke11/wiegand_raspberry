from fastapi import FastAPI

from board import *

board = BOARD()

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Server Raspberry PI"}

@app.get("/open")
async def openDoor():
    board.activateRelay(7,4)
    return {"open Gate":"Opening and Close Door"}
