import httpx
from fastapi import HTTPException
from loguru import logger

from src.config import Config


class BellRingerService:
    async def ring_bell(self, apartment_id: int) -> None:
        """Rings the bell of the apartment."""
        if apartment_id not in Config.AVAILABLE_APARTMENTS_FOR_BELL_RINGING:
            raise HTTPException(status_code=404, detail="Apartment not found")

        headers = {
            "Authorization": f"Bearer {Config.WHATSAPP_ACCESS_TOKEN}",
            "Content-Type": "application/json",
        }

        data = {
            "messaging_product": "whatsapp",
            "to": Config.WHATSAPP_FINAL_NUMBER,
            "type": "template",
            "template": {
                "name": "campainha",
                "language": {"code": "pt_BR"},
                "components": [
                    {
                        "type": "body",
                        "parameters": [
                            {
                                "type": "text",
                                "parameter_name": "apartment_id",
                                "text": f"{apartment_id}",
                            }
                        ],
                    }
                ],
            },
        }

        async with httpx.AsyncClient() as client:
            response = await client.post(
                Config.WHATSAPP_API_URL, json=data, headers=headers
            )
            response.raise_for_status()

        logger.info(f"Ringing the bell of apartment {apartment_id}")
        return None
