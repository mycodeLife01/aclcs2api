from pydantic import BaseModel


class TeamResponse(BaseModel):
    teamId: str
    name: str
    logo: str
