from app.config import settings
from os import environ
import json

from sqlalchemy import create_engine

from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import Session

conn = json.loads(environ['SQLALCHEMY_URL'])

engines = {
    "cypherus_helpdesk": create_engine(conn['cypherus_helpdesk'], pool_pre_ping=True)
}

class RoutingSession(Session):
    def get_bind(self, mapper=None, clause=None):
        if self._name:
            return engines[self._name]
        return super().get_bind(mapper, clause)

    _name = None
    
    def using_bind(self, name):
        print(f"using_bind chamado com name: {name}")
        s = RoutingSession()
        vars(s).update(vars(self))
        s._name = name
        return s

Session = scoped_session(sessionmaker(class_=RoutingSession))
