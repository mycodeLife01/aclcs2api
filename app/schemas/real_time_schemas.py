from pydantic import BaseModel


class PlayerInfo(BaseModel):
    steamId: str
    playerName: str
    kills: int
    deaths: int
    assists: int


class RealTimeTeam(BaseModel):
    playerStats: list[PlayerInfo]
    teamId: str
    teamName: str
    teamScore: int
    

class RealTimeData(BaseModel):
    matchId: str
    matchStatus: int
    team_1: RealTimeTeam
    team_2: RealTimeTeam
    winnerTeam: str
