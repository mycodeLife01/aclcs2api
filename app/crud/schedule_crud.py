from sqlmodel import select, Session
from app.models import Schedule
from fastapi import HTTPException
from ..core.logger import logger


def query_all_schedules(session: Session):
    try:
        statement = select(Schedule).where(Schedule.stage_id.notin_([0, 5]))
        schedules = session.exec(statement).all()
        return schedules
    except Exception as e:
        logger.error(f"Error while querying all schedules: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail="Server error... Please try again later"
        )


def query_schedules_by_season_id(session: Session, season_id: int) -> list[Schedule]:
    try:
        statement = select(Schedule).where(
            Schedule.season_id == season_id, Schedule.stage_id.notin_([0, 5])
        )
        schedules = session.exec(statement).all()
        return schedules
    except Exception as e:
        logger.error(f"Error while querying schedules by season id: {e}", exc_info=True)
        raise HTTPException(
            status_code=500, detail="Server error... Please try again later"
        )


def query_schedules_by_season_ids(session: Session, season_ids: list[int]):
    try:
        statement = select(Schedule).where(
            Schedule.season_id.in_(season_ids), Schedule.stage_id.notin_([0, 5])
        )
        schedules = session.exec(statement).all()
        return schedules
    except Exception as e:
        logger.error(
            f"Error while querying schedules by season ids: {e}", exc_info=True
        )
        raise HTTPException(
            status_code=500, detail="Server error... Please try again later"
        )


def query_current_schedule(session: Session):
    try:
        stmt = select(Schedule).where(Schedule.schedule_status == 2)
        current_schedule = session.exec(stmt).first()
        return current_schedule
    except Exception as e:
        logger.error(f"Error while querying schedules by season id: {e}", exc_info=True)
