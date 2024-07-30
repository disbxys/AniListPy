from enum import Enum
import os


ANILIST_QUERIES_DIR = os.path.join(os.path.dirname(__file__), "queries")


class AniListQuery(Enum):
    ANIME_ID = "anime_id"
    ANIME_IDMAL = "anime_idmal"
    ANIME_MEDIA_PAGE_LIST = "anime_media_page_list"
    ANIME_SEARCH = "anime_search"
    EPISODE_NUMS = "episode_nums"
    MANGA_ID = "manga_id"
    MANGA_IDMAL = "manga_idmal"
    MANGA_MEDIA_PAGE_LIST = "manga_media_page_list"
    MANGA_SEARCH = "manga_search"
    MEDIA_PAGE_LIST = "media_page_list"
    USERDATA = "userdata"


def read_query(query: AniListQuery) -> str:
    """Return a query string from file based on the given query."""
    query_filename = os.path.join(
        ANILIST_QUERIES_DIR,
        query.value + ".graphql"
    )

    with open(query_filename, "r", encoding="utf-8") as qfile:
        query_string = qfile.read().strip()

    return query_string
