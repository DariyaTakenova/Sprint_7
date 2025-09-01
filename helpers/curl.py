import requests
from helpers.data import BASE_URL

def post(endpoint: str, payload: dict = None, use_json: bool = True):

    url = BASE_URL + endpoint
    if use_json:
        return requests.post(url, json=payload)
    else:
        return requests.post(url, data=payload)

def get(endpoint: str, params: dict = None):
    url = BASE_URL + endpoint
    return requests.get(url, params=params)

def delete(endpoint: str):
    url = BASE_URL + endpoint
    return requests.delete(url)
