import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from src.services.riot import get_summoner_uuid, get_matches_history, get_match_stats
from src.services.mongo import favorite_match, delete_match, get_favorite_matches

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")    
def render_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/matches/")
async def get_player_match_history(summoner_name: str = Form(...), request: Request = None):
    if request is None:
        request = Request()

    uuid = get_summoner_uuid(summoner_name)
    if uuid == {"error": "Error getting data from summoner"}:
        return {"message": "Summoner not found."}
    
    matches = get_matches_history(uuid)
    if matches == []:
        return {"message": "No match history found for this summoner."}
    
    matches_stats = []
    for match in matches:
        match_stats = get_match_stats(match, uuid)
        matches_stats.append(match_stats)

    return templates.TemplateResponse("matches.html", {"request": request, "summoner_name": summoner_name, "matches": matches_stats})

@app.post("/favorite/")
async def favorite_match_action(match_id: str, summoner_name: str, map: str, champion_played: str, victory_or_defeat: str, kda: str):
    result = favorite_match(match_id, summoner_name, map, champion_played, victory_or_defeat, kda)
    return result

@app.delete("/delete/")
async def delete_match_action(match_id: str, summoner_name: str):
    result = delete_match(match_id, summoner_name)
    return result

@app.get("/favorites/{summoner_name}")
async def render_favorite_matches(request: Request, summoner_name: str):
    favorite_matches = get_favorite_matches(summoner_name)

    if not favorite_matches:
        return templates.TemplateResponse("favorites.html", {"request": request, "summoner_name": summoner_name, "favorite_matches": [], "message": "Nenhuma partida foi favoritada ainda."})
    
    return templates.TemplateResponse("favorites.html", {"request": request, "summoner_name": summoner_name, "favorite_matches": favorite_matches})

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)