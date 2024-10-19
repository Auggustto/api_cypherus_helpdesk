from fastapi import FastAPI

### import schemas of routers ###
from app.routers.company_routers import company_routers

app = FastAPI()

### include all routers ###
app.include_router(router=company_routers)