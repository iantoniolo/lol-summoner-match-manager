import uvicorn
from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

from src.services.riot import get_summoner_uuid, get_matches_history, get_match_stats

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")    
def render_form(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/match-history/")
def get_player_match_history(summoner_name: str = Form(...)):
    uuid = get_summoner_uuid(summoner_name)
    matches = get_matches_history(uuid)

    matches_stats = []

    for match in matches:
        match_stats = get_match_stats(match, uuid)
        matches_stats.append(match_stats)

    return matches_stats

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)