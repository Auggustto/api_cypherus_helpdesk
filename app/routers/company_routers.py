from fastapi import APIRouter, Depends, status
from starlette.responses import RedirectResponse
from sqlalchemy.orm import Session
from typing import Annotated

from app.models.database.get_session import get_session
from app.controller.company_controller import CompanyController
from app.schemas.user_schemas import MetadaCompany

company_routers = APIRouter(prefix='/helpdesk/api', tags=['Company'])

### create a session ###
SessionDep = Annotated[Session, Depends(get_session)]

@company_routers.get('/', include_in_schema=False)
def documents():
    return RedirectResponse(url='/docs')

@company_routers.post('/company', status_code=status.HTTP_201_CREATED, tags=['Company'], include_in_schema=True)
def test(metadata: MetadaCompany, session: Session = Depends(get_session)):
    return CompanyController().post_company(session=session, metadada=metadata)
