from sqlmodel import select, Session
from ..core.logger import logger
from ..models import Match


def query_all_matches(session: Session):
    try:
        stmt = select(Match)
        matches_all = session.exec(stmt).all()
        return matches_all
    except Exception as e:
        logger.error(f"Error while querying all matches:{e}", exc_info=True)


def query_matches_by_schedule_id(session: Session, schedule_id: str):
    try:
        stmt = select(Match).where(Match.schedule_id == schedule_id)
        matches_by_schedule_id = session.exec(stmt).all()
        return matches_by_schedule_id
    except Exception as e:
        logger.error(f"Error while querying matches by schedule id:{e}", exc_info=True)


def query_matches_by_schedule_ids(session: Session, schedule_ids: list[str]):
    try:
        stmt = select(Match).where(Match.schedule_id.in_(schedule_ids))
        matches_by_schedule_ids = session.exec(stmt).all()
        return matches_by_schedule_ids
    except Exception as e:
        logger.error(f"Error while querying matches by schedule ids:{e}", exc_info=True)


def query_current_match(session: Session):
    try:
        stmt = select(Match).where(Match.match_status == 2)
        current_match = session.exec(stmt).first()
        return current_match
    except Exception as e:
        logger.error(f"Error while querying current match:{e}", exc_info=True)
