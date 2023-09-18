from fastapi import FastAPI
from contact import endpoint
from information import endpoint1
from search import endpoint2

app=FastAPI()

app.include_router(endpoint.router, prefix="/send-email", tags=["send-email"])
app.include_router(endpoint1.router1,prefix="/Information", tags=["Information"])
app.include_router(endpoint2.router2,prefix="/search", tags=["search"])
