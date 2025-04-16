from sqlmodel import Session, select
from ..core.logger import logger
from ..models import Season


def query_all_seasons(session: Session):
    try:
        stmt = select(Season)
        seasons = session.exec(stmt).all()
        return seasons
    except Exception as e:
        logger.error(f"Error while querying all seasons")


def query_seasons_by_start_time(session: Session, start_time: int):
    try:
        stmt = select(Season).where(Season.season_start_time == start_time)
        seasons = session.exec(stmt).all()
        return seasons
    except Exception as e:
        logger.error(f"Error while querying seasons by start time")


def query_seasons_by_end_time(session: Session, end_time: int):
    try:
        stmt = select(Season).where(Season.season_end_time == end_time)
        seasons = session.exec(stmt).all()
        return seasons
    except Exception as e:
        logger.error(f"Error while querying seasons by end time")


def query_seasons_by_start_time_and_end_time(session: Session, start_time: int, end_time: int):
    try:
        stmt = select(Season).where(
            Season.season_end_time == end_time, Season.season_start_time == start_time
        )
        seasons = session.exec(stmt).all()
        return seasons
    except Exception as e:
        logger.error(f"Error while querying seasons by start time and end time")
