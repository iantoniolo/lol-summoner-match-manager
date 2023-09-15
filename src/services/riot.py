from ..config.settings import RIOT_APY_KEY

import requests

def get_summoner_uuid(summoner_name: str):
    url = f"https://br1.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner_name}?api_key={RIOT_APY_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        uuid = data["puuid"]
        return uuid
    else:
        return {"error": "Erro ao obter dados do invocador"}
    
def get_matches_history(uuid: str):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/by-puuid/{uuid}/ids?start=0&count=3&api_key={RIOT_APY_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        matches = response.json()
        return matches
    else:
        return {"error": "Error when searching summoner's match history."}
    
def get_match_stats(match_id: str, uuid: str):
    url = f"https://americas.api.riotgames.com/lol/match/v5/matches/{match_id}?api_key={RIOT_APY_KEY}"
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        game_mode = "Summoners Rift" if data["info"]["gameMode"] == "CLASSIC" else data["info"]["gameMode"]

        for participant in data["info"]["participants"]:
            if participant["puuid"] == uuid:
                champion = participant["championName"]
                kda = f"{participant['kills']}/{participant['deaths']}/{participant['assists']}"
                status_match = "Victory" if participant["win"] == True else "Defeat"
        return {"map": game_mode, "champion": champion, "status_match": status_match, "kda": kda}
    else:
        return {"error": "Error when fetching match statistics."}