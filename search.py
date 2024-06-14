import requests
from .exceptions import APIError, InvalidQueryError
from .utils import validate_query

class SearchAPI:
    BASE_URL = "https://flask-alt-text-generator-teal-eta.vercel.app/scrape"

    def __init__(self):
        pass

    def search(self, query):
        if not validate_query(query):
            raise InvalidQueryError("Invalid query provided.")

        response = requests.get(f"{self.BASE_URL}?query={query}")
        
        if response.status_code != 200:
            raise APIError(f"API returned an error: {response.status_code}")

        return response.json()
