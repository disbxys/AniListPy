import json

from anilistpy import AniList

al_api = AniList()
response = al_api.query_anime_search("hero academy 2nd season")

with open("./output.json", "w+", encoding="utf-8") as outfile:
    json.dump(response, outfile, ensure_ascii=False, indent=4)


# with open("./output.txt", "w+", encoding="utf-8") as outfile:
#     # grouped by reading status
#     for entry_category in response["data"]["MediaListCollection"]["lists"]:
#         # if entry_category["name"] == "Completed":
#         for entry in entry_category["entries"]:
#             outfile.write(entry["media"]["title"]["romaji"] + "\n")