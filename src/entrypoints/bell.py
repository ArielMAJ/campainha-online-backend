from fastapi import APIRouter

from src.services.bell_ringer_service import BellRingerService

router = APIRouter()


@router.post("/bell/{apartment_id}", status_code=200)
async def bell(apartment_id: int) -> None:
    """
    Rings the bell of the apartment.

    It returns 200 if the bell was rung successfully.
    """
    return await BellRingerService().ring_bell(apartment_id)
