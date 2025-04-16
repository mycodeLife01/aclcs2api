from sqlmodel import Session
from ..core.logger import logger
from ..crud.team_crud import *
from ..schemas.team_schemas import *


def get_all_teams(session: Session):
    try:
        teams_all = query_all_teams(session)
        return to_team_response(teams_all)
    except Exception as e:
        logger.error(f"Error while getting all teams:{e}", exc_info=True)


def get_teams_by_schedule_id(session: Session, schedule_id: str):
    try:
        teams_by_schedule_id = query_teams_by_schedule_id(session, schedule_id)
        return to_team_response(teams_by_schedule_id)
    except Exception as e:
        logger.error(f"Error while getting all teams:{e}", exc_info=True)


def get_teams_by_schedule_ids(session: Session, schedule_ids: list[str]):
    try:
        teams_by_schedule_id = query_teams_by_schedule_ids(session, schedule_ids)
        return to_team_response(teams_by_schedule_id)
    except Exception as e:
        logger.error(f"Error while getting all teams:{e}", exc_info=True)


def to_team_response(teams: list[Team]):
    try:
        teams_result = []
        for team in teams:
            team_res = TeamResponse(
                teamId=team.team_id, name=team.team_name, logo=team.team_logo
            )
            teams_result.append(team_res)
        return teams_result
    except Exception as e:
        logger.error(f"Error while transfering to response teams:{e}", exc_info=True)
