from fastapi import APIRouter, Depends, status
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Annotated

from app.models.database.get_session import get_session
from app.controller.user_controller import UserController
from app.schemas.user_schemas import MetadaUser

user_routers = APIRouter(prefix='/helpdesk/api', tags=['Company'])

### create a session ###
SessionDep = Annotated[Session, Depends(get_session)]

@user_routers.get('/', include_in_schema=False)
def documents():
    return RedirectResponse(url='/docs')

@user_routers.post('/user', status_code=status.HTTP_201_CREATED, tags=['User'], include_in_schema=True)
def create(metadata: MetadaUser, session: Session = Depends(get_session)):
    return UserController().post_user(session=session, metadada=metadata)

@user_routers.get('/user/{id}', status_code=status.HTTP_200_OK, tags=['User'], include_in_schema=True)
def read(id: int, session: Session = Depends(get_session)):
    return UserController().read_user(session=session, id=id)

@user_routers.put('/user/{id}', status_code=status.HTTP_200_OK, tags=['User'], include_in_schema=True)
def put(metadata: MetadaUser, id: int,  session: Session = Depends(get_session)):
    return UserController().update_user(session=session, id=id, metadata=metadata)

@user_routers.delete('/user/{id}', status_code=status.HTTP_200_OK, tags=['User'], include_in_schema=True)
def delete(id: int, session: Session = Depends(get_session)):
    return UserController().delete_user(session=session, id=id)

