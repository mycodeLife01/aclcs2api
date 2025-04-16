from fastapi.background import P
from sqlmodel import Session
from ..core.logger import logger
from ..crud.match_crud import *
from ..schemas.match_schemas import MatchResponse


def get_all_matches(session: Session):
    try:
        matches_all = query_all_matches(session)
        return to_match_response(matches_all)
    except Exception as e:
        logger.error(f"Error getting all matches:{e}", exc_info=True)


def get_matches_by_schedule_id(session: Session, schedule_id: str):
    try:
        matches_by_schedule_id = query_matches_by_schedule_id(session, schedule_id)
        return to_match_response(matches_by_schedule_id)
    except Exception as e:
        logger.error(f"Error getting matches by schedule id:{e}", exc_info=True)


def get_matches_by_schedule_ids(session: Session, schedule_ids: list[str]):
    try:
        matches_by_schedule_ids = query_matches_by_schedule_ids(session, schedule_ids)
        return to_match_response(matches_by_schedule_ids)
    except Exception as e:
        logger.error(f"Error getting matches by schedule ids:{e}", exc_info=True)


def to_match_response(matches: list[Match]):
    try:
        # 过滤掉 schedule_id.split('-')[1] 为 '0' 或 '5' 的 match
        filtered_matches = [
            match
            for match in matches
            if len(match.schedule_id.split("-")) > 1
            and match.schedule_id.split("-")[1] not in ("0", "5")
        ]
        match_response = []
        grouped = {}
        for match in filtered_matches:
            schedule_id = match.schedule_id
            if schedule_id not in grouped:
                grouped[schedule_id] = [match]
            else:
                grouped[schedule_id].append(match)
        for schedule_id, match_list in grouped.items():
            match_response.append(
                MatchResponse(scheduleId=schedule_id, matchList=match_list)
            )
        match_response.sort(key=lambda x: tuple(map(int, x.scheduleId.split("-"))))
        for series in match_response:
            series.matchList.sort(key=lambda x: x.match_num)
        return match_response
    except Exception as e:
        logger.error(f"Error while transfering to match response:{e}", exc_info=True)
