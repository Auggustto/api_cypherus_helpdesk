from fastapi import FastAPI

### import schemas of routers ###
from app.routers.user_routers import user_routers

app = FastAPI()

### include all routers ###
app.include_router(router=user_routers)