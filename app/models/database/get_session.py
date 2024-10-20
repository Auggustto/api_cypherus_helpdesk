from fastapi import Depends
from sqlalchemy.orm import Session
from typing import Generator
from app.models.database.db import RoutingSession, Session as SessionLocal

def get_session(name: str = "cypherus_helpdesk") -> Generator[RoutingSession, None, None]:
    db_session = SessionLocal().using_bind(name)
    # db_session = SessionLocal()
    
    try:
        yield db_session
    finally:
        db_session.close()
