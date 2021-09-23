from typing import Optional

from fastapi import FastAPI
from router import genrate

app = FastAPI()

app.include_router(genrate.router)
