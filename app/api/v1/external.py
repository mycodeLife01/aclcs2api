from app.schemas.real_time_schemas import RealTimeData
from app.schemas.schedule_schemas import RealTimeSchedule
from app.services.real_time_service import (
    get_real_time_data,
    get_real_time_schedule_data,
)
from ...schemas.request_schemas import *
from fastapi import APIRouter, Query, Depends
from typing import Annotated
from app.crud.schedule_crud import *
from app.dependencies import SessionDep
from app.core.exceptions import DataNotFoundException
from ...schemas.response_schemas import ResponseWrapper
from ...services.schedule_service import *
from ...services.team_service import *
from ...services.player_service import *
from ...services.season_service import *
from ...services.match_service import *
from ...schemas.match_schemas import MatchResponse

router = APIRouter(
    responses={404: {"description": "Not Found"}, 500: {"description": "Server error"}}
)


@router.get(
    "/schedules",
    response_model=ResponseWrapper[list[SeasonScheduleResponse]],
    tags=["赛程"],
)
def get_schedules(
    session: SessionDep, schedule_query: Annotated[ScheduleQuery, Query()]
):
    season_id = schedule_query.season_id
    season_ids = schedule_query.season_ids
    if season_id is not None:
        schedules_by_season_id = fetch_schedules(session, season_id=season_id)
        if not schedules_by_season_id:
            raise DataNotFoundException(param="season_id")
        return ResponseWrapper(data=schedules_by_season_id)
    if season_ids is not None:
        schedules_by_season_ids = fetch_schedules(session, season_ids=season_ids)
        if not schedules_by_season_ids:
            raise DataNotFoundException(param="season_ids")
        return ResponseWrapper(data=schedules_by_season_ids)
    schedules_all = fetch_schedules(session)
    return ResponseWrapper(data=schedules_all)


@router.get("/teams", response_model=ResponseWrapper[list[TeamResponse]], tags=["队伍"])
def get_teams(session: SessionDep, team_query: Annotated[TeamQuery, Query()]):
    schedule_id = team_query.schedule_id
    schedule_ids = team_query.schedule_ids
    if schedule_id is not None:
        teams_by_schedule_id = fetch_teams(session, schedule_id=schedule_id)
        if not teams_by_schedule_id:
            raise DataNotFoundException(param="schedule_id")
        return ResponseWrapper(data=teams_by_schedule_id)
    if schedule_ids is not None:
        teams_by_schedule_ids = fetch_teams(session, schedule_ids=schedule_ids)
        if not teams_by_schedule_ids:
            raise DataNotFoundException(param="schedule_ids")
        return ResponseWrapper(data=teams_by_schedule_ids)
    teams_all = fetch_teams(session)
    return ResponseWrapper(data=teams_all)


@router.get(
    "/players", response_model=ResponseWrapper[list[PlayerResponse]], tags=["选手"]
)
def get_players(session: SessionDep):
    players_all = get_all_players(session)
    if not players_all:
        raise DataNotFoundException()
    return ResponseWrapper(data=players_all)


@router.get("/seasons", response_model=ResponseWrapper[list[Season]], tags=["赛事"])
def get_seasons(session: SessionDep, season_query: SeasonQuery = Depends()):
    season_start_time = season_query.season_start_time
    season_end_time = season_query.season_end_time
    if None not in (season_start_time, season_end_time):
        seasons_by_start_time_and_end_time = fetch_seasons(
            session, start_time=season_start_time, end_time=season_end_time
        )
        if not seasons_by_start_time_and_end_time:
            raise DataNotFoundException(param="season_start_time, season_end_time")
        return ResponseWrapper(data=seasons_by_start_time_and_end_time)
    elif season_start_time is not None:
        seasons_by_start_time = fetch_seasons(session, start_time=season_start_time)
        if not seasons_by_start_time:
            raise DataNotFoundException(param="season_start_time")
        return ResponseWrapper(data=seasons_by_start_time)
    elif season_end_time is not None:
        seasons_by_end_time = fetch_seasons(session, end_time=season_end_time)
        if not seasons_by_end_time:
            raise DataNotFoundException(param="season_end_time")
        return ResponseWrapper(data=seasons_by_end_time)
    seasons_all = fetch_seasons(session)
    return ResponseWrapper(data=seasons_all)


@router.get(
    "/matches", response_model=ResponseWrapper[list[MatchResponse]], tags=["对局"]
)
def get_matches(session: SessionDep, match_query: Annotated[MatchQuery, Query()]):
    schedule_id = match_query.schedule_id
    schedule_ids = match_query.schedule_ids
    if schedule_id is not None:
        matches_by_schedule_id = fetch_matches(session, schedule_id=schedule_id)
        if not matches_by_schedule_id:
            raise DataNotFoundException(param="schedule_id")
        return ResponseWrapper(data=matches_by_schedule_id)
    if schedule_ids is not None:
        matches_by_schedule_ids = fetch_matches(session, schedule_ids=schedule_ids)
        if not matches_by_schedule_ids:
            raise DataNotFoundException(param="schedule_ids")
        return ResponseWrapper(data=matches_by_schedule_ids)
    matches_all = fetch_matches(session)
    return ResponseWrapper(data=matches_all)


@router.get(
    "/real_time_match", response_model=ResponseWrapper[RealTimeData], tags=["实时对局"]
)
def get_real_time_match(session: SessionDep):
    real_time_match = get_real_time_data(session)
    if not real_time_match:
        raise DataNotFoundException(param="")
    return ResponseWrapper(data=real_time_match)


@router.get(
    "/real_time_schedule",
    response_model=ResponseWrapper[RealTimeSchedule],
    tags=["实时赛程"],
)
def get_real_time_schedule(session: SessionDep):
    real_time_schedule = get_real_time_schedule_data(session)
    if not real_time_schedule:
        raise DataNotFoundException(param="")
    return ResponseWrapper(data=real_time_schedule)
