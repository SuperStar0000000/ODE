from fastapi import APIRouter, HTTPException, Request
import requests

dataset = APIRouter()

@dataset.get('/')
async def root():
    return {"message": "Hello World!"}

@dataset.get("/api")
async def root(request: Request):
    api_url = request.headers.get('api_url')
    print(api_url)
    #response = requests.get(api_url)
    #response_body = response.json()
    return  {"message": "Requesting from url: " + api_url,
            #"response:": response_body
            }