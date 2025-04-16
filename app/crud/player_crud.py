from sqlmodel import Session, select
from ..core.logger import logger
from ..models import Player


def query_all_players(session: Session):
    try:
        stmt = select(Player).where(Player.delete != 1).order_by(Player.team_id)
        players = session.exec(stmt).all()
        return players
    except Exception as e:
        logger.error(f"Error while querying all players:{e}", exc_info=True)
