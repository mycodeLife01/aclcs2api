from sqlmodel import Session
from ..core.logger import logger
from ..crud.team_crud import *
from ..schemas.team_schemas import *
from typing import Optional


def fetch_teams(
    session: Session,
    *,
    schedule_id: Optional[str] = None,
    schedule_ids: Optional[list[str]] = None,
):
    try:
        if schedule_id:
            teams_raw = query_teams_by_schedule_id(session, schedule_id)
        elif schedule_ids:
            teams_raw = query_teams_by_schedule_ids(session, schedule_ids)
        else:
            teams_raw = query_all_teams(session)
        return parse_teams(teams_raw)
    except Exception as e:
        logger.error(f"Error while getting all teams:{e}", exc_info=True)


def parse_teams(teams: list[Team]):
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
