from sqlmodel import Session
from sqlmodel import select
from ..models import RealTimePlayer
from ..core.logger import logger
from ..models import RealTimeMatch

def query_real_time_player(session: Session, match_id: str):
    try:
        stmt = select(RealTimePlayer).where(RealTimePlayer.match_id == match_id)
        players = session.exec(stmt).all()
        return players
    except Exception as e:
        logger.error(f"Error while querying real time player:{e}", exc_info=True)

def query_real_time_match(session: Session, match_id: str):
    try:
        stmt = select(RealTimeMatch).where(RealTimeMatch.match_id == match_id)
        real_time_match = session.exec(stmt).first()
        return real_time_match
    except Exception as e:
        logger.error(f"Error while querying real time match:{e}", exc_info=True)