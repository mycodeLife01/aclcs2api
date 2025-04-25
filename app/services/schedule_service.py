from operator import attrgetter
from pickle import TRUE

from sqlalchemy import true
from ..crud.schedule_crud import *
from sqlmodel import Session
from ..core.logger import logger
from ..schemas.schedule_schemas import (
    ScheduleResponse,
    TeamScore,
    SeasonScheduleResponse,
)
from itertools import groupby
from typing import Optional


def fetch_schedules(
    session: Session,
    *,
    season_id: Optional[int] = None,
    season_ids: Optional[list[int]] = None,
) -> list[Schedule]:
    try:
        if season_id is not None:
            raw = query_schedules_by_season_id(session, season_id)
        elif season_ids is not None:
            raw = query_schedules_by_season_ids(session, season_ids)
        else:
            raw = query_all_schedules(session)
        return parse_schedules(raw)
    except Exception as e:
        logger.error(
            f"Error while getting schedules: (season_id={season_id}, season_ids={season_ids}): {e}",
            exc_info=True,
        )
        return []


def parse_schedules(schedules: list[Schedule]) -> list[SeasonScheduleResponse]:
    if not schedules:
        return []
    schedules_sorted = sorted(
        schedules,
        key=lambda s: (s.season_id, tuple(map(int, s.schedule_id.split("-")))),
    )
    result: list[SeasonScheduleResponse] = []
    for season_id, grouped_schedules in groupby(
        schedules_sorted, key=attrgetter("season_id")
    ):
        schedule_list = [
            ScheduleResponse(
                scheduleId=s.schedule_id,
                scheduleName=s.schedule_name,
                scheduleType=s.schedule_type,
                scheduleStatus=s.schedule_status,
                teamScoreList=[
                    TeamScore(teamId=s.team_1, score=s.team_1_score),
                    TeamScore(teamId=s.team_2, score=s.team_2_score),
                ],
                stageId=s.stage_id,
                stageName=s.stage_name,
                scheduleStartTime=s.schedule_start_time,
                scheduleRealStartTime=s.schedule_real_start_time,
                scheduleRealEndTime=s.schedule_real_end_time,
            )
            for s in grouped_schedules
        ]
        result.append(
            SeasonScheduleResponse(seasonId=season_id, scheduleList=schedule_list)
        )
    return result
