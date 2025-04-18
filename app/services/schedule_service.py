from ..crud.schedule_crud import *
from sqlmodel import Session
from ..core.logger import logger
from ..schemas.schedule_schemas import (
    ScheduleResponse,
    TeamScore,
    SeasonScheduleResponse,
)


def get_all_schedules(session: Session):
    try:
        return sort_schedules_by_season(query_all_schedules(session))
    except Exception as e:
        logger.error(f"Error while getting all schedules:{e}", exc_info=True)
        return []


def get_schedules_by_season_id(session: Session, season_id: int):
    try:
        return sort_schedules_by_season(query_schedules_by_season_id(session, season_id))
    except Exception as e:
        logger.error(f"Error while getting schedules by season id:{e}", exc_info=True)
        return []
    
def get_schedules_by_season_ids(session: Session, season_ids: list[int]):
    try:
        return sort_schedules_by_season(query_schedules_by_season_ids(session, season_ids))
    except Exception as e:
        logger.error(f"Error while getting schedules by season id:{e}", exc_info=True)
        return []


def sort_schedules_by_season(schedules: list[Schedule]):
    if not schedules:
        return {}
    grouped = {}
    result = []
    try:
        for s in schedules:
            season_id = s.season_id
            if season_id not in grouped:
                grouped[season_id] = [s]
            else:
                grouped[season_id].append(s)
        for season_id, schedules in grouped.items():
            schedule_list = []
            for schedule in schedules:
                team_score_list = []
                team_1_data = TeamScore(
                    teamId=schedule.team_1, score=schedule.team_1_score
                )
                team_2_data = TeamScore(
                    teamId=schedule.team_2, score=schedule.team_2_score
                )
                team_score_list.extend([team_1_data, team_2_data])
                schedule_res = ScheduleResponse(
                    scheduleId=schedule.schedule_id,
                    scheduleName=schedule.schedule_name,
                    scheduleType=schedule.schedule_type,
                    teamScoreList=team_score_list,
                    scheduleStatus=schedule.schedule_status,
                    stageId=schedule.stage_id,
                    stageName=schedule.stage_name,
                    scheduleStartTime=schedule.schedule_start_time,
                    scheduleRealStartTime=schedule.schedule_real_start_time,
                    scheduleRealEndTime=schedule.schedule_real_end_time,
                )
                schedule_list.append(schedule_res)
            season_schedule_res = SeasonScheduleResponse(
                seasonId=season_id, scheduleList=schedule_list
            )
            result.append(season_schedule_res)
        result.sort(key=lambda item: item.seasonId)
        for r in result:
            schedule_list = r.scheduleList
            schedule_list.sort(key=lambda s: tuple(map(int, s.scheduleId.split("-"))))
        return result
    except Exception as e:
        logger.error(f"Error while sorting schedules:{e}", exc_info=True)
        return {}
