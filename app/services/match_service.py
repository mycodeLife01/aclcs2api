from collections import defaultdict
from typing import Optional
from fastapi.background import P
from sqlmodel import Session
from ..core.logger import logger
from ..crud.match_crud import *
from ..schemas.match_schemas import MatchResponse


def fetch_matches(
    session: Session,
    *,
    schedule_id: Optional[int] = None,
    schedule_ids: Optional[list[int]] = None,
):
    try:
        if schedule_id is not None:
            raw = query_matches_by_schedule_id(session, schedule_id)
        elif schedule_ids is not None:
            raw = query_matches_by_schedule_ids(session, schedule_ids)
        else:
            raw = query_all_matches(session)
        return parse_matches(raw)
    except Exception as e:
        logger.error(
            f"Error while getting matches (schedule_id:{schedule_id}, schedule_ids:{schedule_ids}):{e}",
            exc_info=True,
        )
        return []


def parse_matches(matches: list[Match]):
    if not matches:
        return []
    filtered_matches = [
        m for m in matches if m.match_id.split("-")[1] not in (["0", "5", "6"])
    ]
    result: list[MatchResponse] = []
    group = defaultdict(list)
    for match in filtered_matches:
        group[match.schedule_id].append(match)
    for schedule_id, matches in group.items():
        matches.sort(key=lambda m: m.match_num)
        result.append(MatchResponse(scheduleId=schedule_id, matchList=matches))
    result.sort(key=lambda mr: tuple(map(int, mr.scheduleId.split("-"))))
    return result
