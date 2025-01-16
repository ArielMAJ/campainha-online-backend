from fastapi.routing import APIRouter

from src.entrypoints import bell, monitoring

router = APIRouter()
router.include_router(monitoring.router, tags=["Monitoring"])
router.include_router(bell.router, tags=["Bell"])
