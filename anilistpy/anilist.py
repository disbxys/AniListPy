from urllib.parse import urlparse

import requests

from . import query as al_query

class InvalidVariableError(Exception):
    pass

class AniList:
    def __init__(self, driver=None):
        if not driver:
            self.session = driver
        else:
            self.session = requests.session()

        self.api_endpoint = "https://graphql.anilist.co"
        
        # TODO: implement way to limit requests.

    def query_user(self, username, media_type="ANIME"):
        variables = {
            "username": username,
            "type": media_type if media_type in ("ANIME", "MANGA") else "ANIME"
        }
        req = self.send_request(al_query.USERDATA, variables)

        return req.json()

    def query_manga_id(self, id:int):
        variables = { "id": id }
        req = self.send_request(al_query.MANGA_ID, variables)
        return req.json()

    def query_manga_idMal(self, id:int):
        variables = { "idMal": id }
        req = self.send_request(al_query.MANGA_IDMAL, variables)
        return req.json()
    
    def query_manga_search(self, keyword:str):
        variables = { "search": keyword }
        req = self.send_request(al_query.MANGA_SEARCH, variables)
        return req.json()

    def query_episodes(self, id:int):
        query = al_query.episode_names
        variables = { "id": id }

        req = self.send_request(query, variables)

        return req.json()

    def query_anime_id(self, id:int):
        variables = { "id": id }
        req = self.send_request(al_query.ANIME_ID, variables)
        return req.json()

    def query_anime_idMal(self, id:int):
        variables = { "idMal": id }
        req = self.send_request(al_query.ANIME_IDMAL, variables)
        return req.json()
    
    def query_anime_search(self, keyword:str):
        variables = { "search": keyword }
        req = self.send_request(al_query.ANIME_SEARCH, variables)
        return req.json()

    def query_page(self, page_num:int=1, media_type:str="ANIME"):
        variables = {
            "page": page_num,
            "type": media_type if media_type in ("ANIME", "MANGA") else "ANIME"
        }
        req = self.send_request(al_query.MEDIA_PAGE_LIST, variables)

        return req.json()

    def send_request(self, query, variables):
        req = requests.post(
            self.api_endpoint,
            json={
                "query": query,
                "variables": variables
            }
        )
        return req