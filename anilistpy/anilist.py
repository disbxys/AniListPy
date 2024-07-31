from enum import Enum
import json
from typing import Any, Mapping

import requests
from requests_ratelimiter import Duration, RequestRate, Limiter, LimiterSession

from anilistpy.exceptions import APIException, InvalidMediaTypeError

from anilistpy.qreader import AniListQuery, read_query


class AniListMediaType(Enum):
    anime = "ANIME"
    manga = "MANGA"


    @classmethod
    def of(cls, value: str) -> "AniListMediaType":
        value = value.strip().lower()
        for media_type in cls:
            if media_type.name == value:
                return media_type
        
        raise InvalidMediaTypeError


class AniList:
    PER_PAGE = 50

    def __init__(self, driver: requests.Session | None = None):
        self.session = driver or self._create_session()

        self.api_endpoint = "https://graphql.anilist.co"
        

    def query_user(self, username, media_type = "ANIME") -> dict[str, Any]:
        variables = {
            "username": username,
            "type": media_type if media_type in ("ANIME", "MANGA") else "ANIME"
        }
        return self._post(
            read_query(AniListQuery.USERDATA),
            variables
        )
    

    def query_manga_id(self, id: int) -> dict[str, Any]:
        variables = { "id": id }
        return self._post(
            read_query(AniListQuery.MANGA_ID),
            variables
        )
    

    def query_manga_idMal(self, id: int) -> dict[str, Any]:
        variables = { "idMal": id }
        return self._post(
            read_query(AniListQuery.MANGA_IDMAL),
            variables
        )
    
    
    def query_manga_search(self, keyword: str) -> dict[str, Any]:
        variables = { "search": keyword }
        return self._post(
            read_query(AniListQuery.MANGA_SEARCH),
            variables
        )
        

    def query_episodes(self, id: int) -> dict[str, Any]:
        variables = { "id": id }
        return self._post(
            read_query(AniListQuery.EPISODE_NUMS),
            variables
        )
    

    def query_anime_id(self, id: int) -> dict[str, Any]:
        variables = { "id": id }
        return self._post(
            read_query(AniListQuery.ANIME_ID),
            variables
        )


    def query_anime_idMal(self, id: int) -> dict[str, Any]:
        variables = { "idMal": id }
        return self._post(
            read_query(AniListQuery.ANIME_IDMAL),
            variables
        )
    

    def query_anime_search(self, keyword: str) -> dict[str, Any]:
        variables = { "search": keyword }
        return self._post(
            read_query(AniListQuery.ANIME_SEARCH),
            variables
        )


    def query_page(
            self,
            page_num: int = 1,
            per_page: int = PER_PAGE,
            media_type: AniListMediaType | str = AniListMediaType.anime,
            sort_new: bool = False
    ) -> dict[str, Any]:
        if not isinstance(media_type, AniListMediaType):
            media_type = AniListMediaType.of(media_type)
    
        try:
            variables = {
                "page": page_num,
                "perPage": per_page,
                "type": media_type.value,
                "sort": "ID_DESC" if sort_new else "ID"
            }
        except ValueError:
            raise InvalidMediaTypeError
        

        match media_type:
            case AniListMediaType.anime:
                query = AniListQuery.ANIME_MEDIA_PAGE_LIST
            case AniListMediaType.manga:
                query = AniListQuery.MANGA_MEDIA_PAGE_LIST

        return self._post(read_query(query), variables)
    

    def _post(self, query: str, variables: Mapping[str, Any]) -> dict[str, Any]:
        response = self.session.post(
            self.api_endpoint,
            json={
                "query": query,
                "variables": variables
            },
            verify=False
        )
        return self._wrap_response(response, self.api_endpoint, **variables)
    

    @staticmethod
    def _wrap_response(
        response: requests.Response,
        url: str,
        **kwargs: int | str | None
    ) -> dict[str, Any]:
        
        json_response: dict[str, Any] = {}

        try:
            json_response = response.json()
            if not isinstance(json_response, dict):
                json_response = {"data": json_response}

        except json.JSONDecodeError:
            json_response = {"error": response.text}

        if response.status_code >= 400:
            raise APIException(response.status_code, json_response, **kwargs)
                
        json_response["api_url"] = url
        json_response["headers"] = dict(response.headers)

        return json_response
    

    @staticmethod
    def _create_session() -> LimiterSession:
        mal_rate = RequestRate(90, Duration.MINUTE+1)
        limiter = Limiter(mal_rate)
        session = LimiterSession(limiter=limiter)
        return session