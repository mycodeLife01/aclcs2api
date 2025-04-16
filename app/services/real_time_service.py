from app.crud.match_crud import query_current_match
from app.crud.schedule_crud import query_current_schedule
from app.schemas.real_time_schemas import PlayerInfo, RealTimeData, RealTimeTeam
from app.schemas.schedule_schemas import RealTimeSchedule
from ..crud.real_time_crud import *
from ..core.logger import logger
from sqlmodel import Session


def get_real_time_data(session: Session):
    try:
        current_match = query_current_match(session)
        if not current_match:
            return None
        match_id = current_match.match_id
        real_time_match = query_real_time_match(session, match_id)
        team_1 = real_time_match.team_1
        team_2 = real_time_match.team_2
        team_1_score = real_time_match.team_1_score
        team_2_score = real_time_match.team_2_score
        real_time_players = query_real_time_player(session, match_id)
        team_1_list = []
        team_2_list = []
        for player in real_time_players:
            team = player.team
            player_info = PlayerInfo(
                steamId=player.steam_id,
                playerName=player.player_name,
                kills=player.kills,
                deaths=player.deaths,
                assists=player.assists,
            )
            if team == team_1:
                team_1_list.append(player_info)
            else:
                team_2_list.append(player_info)
        team_1_data = RealTimeTeam(
            teamId=team_1,
            teamName=team_1,
            teamScore=team_1_score,
            playerStats=team_1_list,
        )
        team_2_data = RealTimeTeam(
            teamId=team_2,
            teamName=team_2,
            teamScore=team_2_score,
            playerStats=team_2_list,
        )
        real_time_data = RealTimeData(
            matchId=current_match.match_id,
            team_1=team_1_data,
            team_2=team_2_data,
            matchStatus=current_match.match_status,
            winnerTeam=current_match.winner,
        )
        return real_time_data
    except Exception as e:
        logger.error(f"Error getting real time data:{e}", exc_info=True)


def get_real_time_schedule_data(session: Session):
    try:
        current_schedule = query_current_schedule(session)
        if current_schedule:
            real_time_schedule = RealTimeSchedule(
                scheduleId=current_schedule.schedule_id,
                scheduleName=current_schedule.schedule_name,
                scheduleType=current_schedule.schedule_type,
                team_1=current_schedule.team_1,
                team_2=current_schedule.team_2,
                team_1_score=current_schedule.team_1_score,
                team_2_score=current_schedule.team_2_score,
            )
            return real_time_schedule
        return None
    except Exception as e:
        logger.error(f"Error getting real time schedule data:{e}", exc_info=True)
