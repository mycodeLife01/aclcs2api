from sqlmodel import Session
from ..core.logger import logger
from ..crud.season_crud import *


def get_all_seasons(session: Session):
    try:
        seasons_all = query_all_seasons(session)
        return seasons_all
    except Exception as e:
        logger.error(f"Error while querying all seasons:{e}", exc_info=True)


def get_seasons_by_start_time(session: Session, start_time: int):
    try:
        seasons_by_start_time = query_seasons_by_start_time(session, start_time)
        return seasons_by_start_time
    except Exception as e:
        logger.error(f"Error while querying seasons by start time:{e}", exc_info=True)


def get_seasons_by_end_time(session: Session, end_time: int):
    try:
        seasons_by_end_time = query_seasons_by_end_time(session, end_time)
        return seasons_by_end_time
    except Exception as e:
        logger.error(f"Error while querying seasons by end time:{e}", exc_info=True)


def get_seasons_by_start_time_and_end_time(
    session: Session, start_time: int, end_time: int
):
    try:
        seasons_by_start_time_and_end_time = query_seasons_by_start_time_and_end_time(
            session, start_time, end_time
        )
        return seasons_by_start_time_and_end_time
    except Exception as e:
        logger.error(
            f"Error while querying seasons by start time and end time:{e}",
            exc_info=True,
        )
