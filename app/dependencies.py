from sqlmodel import Session, create_engine
from typing import Annotated
from fastapi import Depends
from app.core.config import DB_CONN_URL

engine = create_engine(url=DB_CONN_URL, echo=True)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
