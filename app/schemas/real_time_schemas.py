from pydantic import BaseModel, Field


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
    matchStatus: int = Field(description="对局状态,1-未开始,2-进行中,3-已结束")
    team_1: RealTimeTeam
    team_2: RealTimeTeam
    winnerTeam: str
