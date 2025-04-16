from sqlmodel import select, Session
from app.models import Schedule, Team
from fastapi import HTTPException
from ..core.logger import logger


def query_all_teams(session: Session):
    try:
        statement = select(Team).where(Team.delete != 1)
        teams = session.exec(statement).all()
        return teams
    except Exception as e:
        logger.error(f"Error while querying all teams:{e}", exc_info=True)


def query_teams_by_schedule_id(session: Session, schedule_id: str):
    try:
        schedule = session.exec(
            select(Schedule).where(Schedule.schedule_id == schedule_id)
        ).first()
        teams = [schedule.team_1, schedule.team_2]
        statement = select(Team).where(Team.team_id.in_(teams))
        result_teams = session.exec(statement).all()
        return result_teams
    except Exception as e:
        logger.error(f"Error while querying teams by schedule id:{e}", exc_info=True)


def query_teams_by_schedule_ids(session: Session, schedule_ids: list[str]):
    try:
        schedules = session.exec(
            select(Schedule).where(Schedule.schedule_id.in_(schedule_ids))
        ).all()
        teams_set = set()
        for schedule in schedules:
            teams_set.add(schedule.team_1)
            teams_set.add(schedule.team_2)
        statement = select(Team).where(Team.team_id.in_(teams_set))
        result_teams = session.exec(statement).all()
        return result_teams
    except Exception as e:
        logger.error(f"Error while querying teams by schedule ids:{e}", exc_info=True)
