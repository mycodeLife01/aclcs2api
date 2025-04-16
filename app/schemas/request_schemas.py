from pydantic import BaseModel, Field
from typing import Optional, Any


class ScheduleQuery(BaseModel):
    season_id: Optional[int] = Field(None, description="查询赛程对应的赛季,Integer类型")
    season_ids: Optional[list[int]] = Field(
        None,
        description="查询赛程对应的多个赛季,List类型",
    )
    class Config:
        extra = "forbid"


class TeamQuery(BaseModel):
    season_id: Optional[int] = Field(None, description="查询队伍对应的赛季,Integer类型")
    season_ids: Optional[list[int]] = Field(
        None,
        description="查询队伍对应的多个赛季,List类型",
    )
    schedule_id: Optional[str] = Field(
        None, description="以该赛程查询对应的队伍,String类型"
    )
    schedule_ids: Optional[list[str]] = Field(
        None,
        description="以该多个赛程查询对应的队伍,List类型",
    )
    class Config:
        extra = "forbid"


class SeasonQuery(BaseModel):
    season_start_time: Optional[int] = Field(None, description="赛事开始时间")
    season_end_time: Optional[int] = Field(None, description="赛事结束时间")
    class Config:
        extra = "forbid"


class MatchQuery(BaseModel):
    schedule_id: Optional[str] = Field(None, description="一个赛程对应的Match")
    schedule_ids: Optional[list[str]] = Field(None, description="多个赛程对应的Match")
