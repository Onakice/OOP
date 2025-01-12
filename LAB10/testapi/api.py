from fastapi import FastAPI, Body
from main import *
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
]

app