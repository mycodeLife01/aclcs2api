from pydantic import BaseModel
from typing import Optional

class PlayerResponse(BaseModel):
    playerName: str
    teamId: str
    photo: str