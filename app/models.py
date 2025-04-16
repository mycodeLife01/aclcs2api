from sqlalchemy import table, true
from sqlmodel import SQLModel, Field
from typing import Optional


class Schedule(SQLModel, table=True):
    schedule_id: str = Field(primary_key=True)
    schedule_name: str
    schedule_status: Optional[int] = 1
    season_id: int
    schedule_start_time: Optional[int] = 0
    schedule_real_start_time: Optional[int] = 0
    schedule_real_end_time: Optional[int] = 0
    team_1: str
    team_2: str
    team_1_score: Optional[int] = 0
    team_2_score: Optional[int] = 0
    schedule_type: int
    stage_id: int
    stage_name: str


class Team(SQLModel, table=True):
    __tablename__ = "team_offline"
    team_id: str = Field(primary_key=True)
    team_name: str
    team_name_abbr: str
    team_logo: str
    region: str
    delete: int


class Player(SQLModel, table=True):
    __tablename__ = "player_offline"
    steam_id: str = Field(primary_key=True)
    char_name: str
    position: str
    starter: int
    team_id: str
    profile_photo: str
    region: str
    delete: int


class Season(SQLModel, table=True):
    __tablename__ = "season"
    season_id: int = Field(primary_key=True)
    season_name: str
    season_start_time: int
    season_end_time: int


class Match(SQLModel, table=True):
    __tablename__ = "match"
    match_id: str = Field(primary_key=True)
    schedule_id: str
    match_start_time: int
    match_end_time: int
    match_real_start_time: int
    match_real_end_time: int
    match_status: int
    match_num: int
    winner: str


class RealTimeMatch(SQLModel, table=True):
    __tablename__ = "real_time_match"
    match_id: str = Field(primary_key=True)
    team_1: str
    team_2: str
    team_1_score: Optional[int] = 0
    team_2_score: Optional[int] = 0


class RealTimePlayer(SQLModel, table=True):
    __tablename__ = "real_time_player"
    match_id: str = Field(primary_key=True)
    steam_id: str = Field(primary_key=True)
    team: str
    player_name: str
    kills: int
    deaths: int
    assists: int
