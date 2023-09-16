from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError

from ..models.player_history import PlayerHistory
from ..config.settings import CLUSTER_URI

client = MongoClient(CLUSTER_URI)
db = client.lol_db
matches_collection = db.players_history

def favorite_match(match_id: str, summoner_name: str, map: str, champion_played: str, victory_or_defeat: str, kda: str):
    try:
        match_data = {
             "match_id": match_id, 
             "summoner_name": summoner_name, 
             "map": map, 
             "champion_played": champion_played, 
             "victory_or_defeat": victory_or_defeat,
             "kda": kda
             }
        matches_collection.insert_one(match_data)
        return {"message": "Match favorited successfully"}
    except DuplicateKeyError:
        return {"error": "Match is already favorited"}

def delete_match(match_id: str, summoner_name: str):
    matches_collection.delete_one({"match_id": match_id, "summoner_name": summoner_name})
    return {"message": "Match deleted successfully"}

def get_favorite_matches(summoner_name: str):
    favorite_matches = matches_collection.find({"summoner_name": summoner_name})

    favorite_matches_data = []

    for match in favorite_matches:
        match_data = {
            "map": match["map"],
            "champion_played": match["champion_played"],
            "victory_or_defeat": match["victory_or_defeat"],
            "kda": match["kda"],
        }
        favorite_matches_data.append(PlayerHistory(**match_data))

    return favorite_matches_data