from enum import Enum
from typing import Any

import requests
from requests_ratelimiter import Duration, RequestRate, Limiter, LimiterSession

from . import query as al_query

class InvalidVariableError(Exception):
    pass

class InvalidMediaTypeError(Exception):
    pass

class AniListMediaType(Enum):
    anime = "ANIME"
    manga = "MANGA"

class AniList:
    PER_PAGE = 50

    def __init__(self, driver: requests.Session | None = None):
        if not driver:
            self.session = self._create_session()
        else:
            self.session = driver

        self.api_endpoint = "https://graphql.anilist.co"
        

    def query_user(self, username, media_type = "ANIME") -> dict[str, Any]:
        variables = {
            "username": username,
            "type": media_type if media_type in ("ANIME", "MANGA") else "ANIME"
        }
        req = self.send_request(al_query.USERDATA, variables)

        return req.json()
    

    def query_manga_id(self, id: int) -> dict[str, Any]:
        variables = { "id": id }
        req = self.send_request(al_query.MANGA_ID, variables)
        return req.json()
    

    def query_manga_idMal(self, id: int) -> dict[str, Any]:
        variables = { "idMal": id }
        req = self.send_request(al_query.MANGA_IDMAL, variables)
        return req.json()
    
    
    def query_manga_search(self, keyword: str) -> dict[str, Any]:
        variables = { "search": keyword }
        req = self.send_request(al_query.MANGA_SEARCH, variables)
        return req.json()
        

    def query_episodes(self, id: int) -> dict[str, Any]:
        query = al_query.EPISODE_NUMS
        variables = { "id": id }

        req = self.send_request(query, variables)

        return req.json()
    

    def query_anime_id(self, id: int) -> dict[str, Any]:
        variables = { "id": id }
        req = self.send_request(al_query.ANIME_ID, variables)
        return req.json()


    def query_anime_idMal(self, id: int) -> dict[str, Any]:
        variables = { "idMal": id }
        req = self.send_request(al_query.ANIME_IDMAL, variables)
        return req.json()
    

    def query_anime_search(self, keyword: str) -> dict[str, Any]:
        variables = { "search": keyword }
        req = self.send_request(al_query.ANIME_SEARCH, variables)
        return req.json()


    def query_page(
            self,
            page_num: int = 1,
            per_page: int = PER_PAGE,
            media_type: AniListMediaType = AniListMediaType.anime,
            sort_new: bool = False
    ) -> dict[str, Any]:
        try:
            variables = {
                "page": page_num,
                "perPage": per_page,
                "type": media_type.value if type(media_type)==AniListMediaType else AniListMediaType(media_type).value,
                "sort": "ID_DESC" if sort_new else "ID"
            }
        except ValueError:
            raise InvalidMediaTypeError
        
        req = self.send_request(al_query.MEDIA_PAGE_LIST, variables)
        resp = req.json()

        # Do not bother filtering data if error detected
        if "errors" not in resp.keys():
            for media in resp["data"]["Page"]["media"]:
                # Remove manga/anime specific information from each entry
                # if looking up anime/manga
                if media_type == "ANIME":
                    media.pop("chapters", None)
                    media.pop("volumes", None)
                elif media_type == "MANGA":
                    media.pop("duration", None)
                    media.pop("episodes", None)
                    media.pop("season", None)
                    media.pop("seasonYear", None)
                    media.pop("studios", None)

        return resp

    def send_request(self, query, variables) -> requests.Response:
        req = self.session.post(
            self.api_endpoint,
            json={
                "query": query,
                "variables": variables
            }
        )
        return req

    @staticmethod
    def _create_session() -> LimiterSession:
        mal_rate = RequestRate(90, Duration.MINUTE+1)
        limiter = Limiter(mal_rate)
        session = LimiterSession(limiter=limiter)
        return session