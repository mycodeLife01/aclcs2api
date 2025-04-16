from pydantic import BaseModel
from typing import Optional
from ..models import Match


class MatchResponse(BaseModel):
    scheduleId: str
    matchList: list[Match]
