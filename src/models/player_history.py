from pydantic import BaseModel

class PlayerHistory(BaseModel):
    map: str
    champion_played: str
    victory_or_defeat: str
    kda: str