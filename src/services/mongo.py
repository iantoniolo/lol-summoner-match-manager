from fastapi import FastAPI, HTTPException

from typing import List

from bson import ObjectId
from pymongo import MongoClient
from config.settings import CLUSTER_URI

from ..models.player_history import PlayerHistory

app = FastAPI()

client = MongoClient(CLUSTER_URI)
db = client.lol_db
players_history_collection = db.players_history

# Criar um novo item no banco de dados
@app.post("/history-player/", response_model=PlayerHistory)
async def register_match(item: PlayerHistory):
    new_match = {"name": item.name, "description": item.description}
    result = players_history_collection.insert_one(new_match)
    created_match = players_history_collection.find_one({"_id": result.inserted_id})
    return created_match

# Obter todos os itens do banco de dados
@app.get("/history-player/", response_model=List[PlayerHistory])
async def get_matches(skip: int = 0, limit: int = 10):
    matches = list(players_history_collection.find().skip(skip).limit(limit))
    return matches

# Obter um item específico por ID
@app.get("/history-player/{player_id}/", response_model=PlayerHistory)
async def get_matches_by_id(player_id: str):
    match = players_history_collection.find_one({"_id": ObjectId(player_id)})
    if match is None:
        raise HTTPException(status_code=404, detail="match not found")
    return match

# Excluir um item específico por ID
@app.delete("/history-player/{player_id}/", response_model=PlayerHistory)
async def delete_match(player_id: str):
    match = players_history_collection.find_one({"_id": ObjectId(player_id)})
    if match is None:
        raise HTTPException(status_code=404, detail="match not found")
    result = players_history_collection.delete_one({"_id": ObjectId(player_id)})
    return match