from ..crud.player_crud import *
from sqlmodel import Session
from ..schemas.player_shemas import PlayerResponse


def get_all_players(session: Session):
    try:
        players_all = query_all_players(session)
        return to_player_response(players_all)
    except Exception as e:
        logger.error(f"Error while querying all players:{e}", exc_info=True)


def to_player_response(players: list[Player]):
    try:
        player_response_list = [
            PlayerResponse(
                playerName=p.char_name, teamId=p.team_id, photo=p.profile_photo
            )
            for p in players
        ]
        return player_response_list
    except Exception as e:
        logger.error(f"Error while transfering to player response:{e}", exc_info=True)
