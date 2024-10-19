from fastapi import APIRouter
from starlette.responses import RedirectResponse


user_routers = APIRouter()

@user_routers.get('/', include_in_schema=True)
def documents():
    return RedirectResponse(url='/docs')