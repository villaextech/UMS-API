from fastapi import FastAPI
from contact import endpoint
from information import endpoint1
#from fastapi.responses import JSONResponse

app=FastAPI()

#app.default_response_class = JSONResponse
app.include_router(endpoint.router, prefix="/send-email", tags=["send-email"])
app.include_router(endpoint1.router1,prefix="/Information", tags=["Information"])
