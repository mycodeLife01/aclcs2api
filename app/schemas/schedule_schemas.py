from pydantic import BaseModel
from typing import Optional


class TeamScore(BaseModel):
    teamId: str
    score: int


class ScheduleResponse(BaseModel):
    scheduleId: str
    scheduleName: str
    teamScoreList: list[TeamScore]
    scheduleStatus: int
    stageId: Optional[int] = None
    stageName: Optional[str] = None
    scheduleStartTime: int
    scheduleRealStartTime: int
    scheduleRealEndTime: int


class SeasonScheduleResponse(BaseModel):
    seasonId: int
    scheduleList: list[ScheduleResponse]


class RealTimeSchedule(BaseModel):
    scheduleId: str
    scheduleName: str
    scheduleType: int
    team_1: str
    team_2: str
    team_1_score: int
    team_2_score: int
