from dataclasses import field
from pydantic import BaseModel, Field
from typing import Optional

from sqlmodel import desc


class TeamScore(BaseModel):
    teamId: str = Field(description="队伍ID")
    score: int = Field(description="比分")


class ScheduleResponse(BaseModel):
    scheduleId: str = Field(description="赛程唯一ID")
    scheduleName: str = Field(description="赛程名")
    scheduleType: int = Field(description="赛程类型,1-BO1,2-BO3")
    teamScoreList: list[TeamScore] = Field(description="队伍比分列表")
    scheduleStatus: int = Field(description="赛程状态,1未开始,2正在进行,3已结束")
    stageId: Optional[int] = Field(None, description="赛事阶段唯一ID")
    stageName: Optional[str] = Field(None, description="赛事阶段名")
    scheduleStartTime: int = Field(description="赛事开始时间")
    scheduleRealStartTime: int = Field(description="赛事真实开始时间")
    scheduleRealEndTime: int = Field(description="赛事真实结束时间")


class SeasonScheduleResponse(BaseModel):
    seasonId: int = Field(description="赛事ID")
    scheduleList: list[ScheduleResponse] = Field(description="赛事对应的赛程列表")


class RealTimeSchedule(BaseModel):
    scheduleId: str 
    scheduleName: str
    scheduleType: int = Field(description="赛程类型,1-BO1,2-BO3")
    team_1: str = Field(description="队伍ID")
    team_2: str
    team_1_score: int
    team_2_score: int
