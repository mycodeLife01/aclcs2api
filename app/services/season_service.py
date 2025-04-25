from sqlmodel import Session
from ..core.logger import logger
from ..crud.season_crud import *
from typing import Optional


def fetch_seasons(
    session: Session, *, start_time: Optional[int] = None, end_time: Optional[int] = None
) -> list[Season]:
    try:
        if None not in (start_time, end_time):
            return query_seasons_by_start_time_and_end_time(
                session, start_time, end_time
            )
        if start_time is not None:
            return query_seasons_by_start_time(session, start_time)
        if end_time is not None:
            return query_seasons_by_end_time(session, end_time)
        return query_all_seasons(session)
    except Exception as e:
        logger.error(
            f"Error while getting seasons (start_time: {start_time}, end_time: {end_time}): {e}"
        )
        return []
