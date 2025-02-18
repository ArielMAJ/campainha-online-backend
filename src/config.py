"""
Application's and its environment's configuration.
"""

import os


class Config:
    """Base configuration."""

    ENVIRONMENT = os.getenv("ENVIRONMENT", "DEV")
    DEBUG = ENVIRONMENT == "DEV"
    TESTING = ENVIRONMENT == "TEST"

    HOST = os.getenv("APPLICATION_HOST", "127.0.0.1")
    PORT = int(os.getenv("APPLICATION_PORT", "3000"))
    WORKERS_COUNT = int(os.getenv("WORKERS_COUNT", "1"))
    RELOAD = os.getenv("RELOAD", "true").lower() == "true"
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")

    APPLICATION_ROOT = os.getenv("APPLICATION_ROOT", "")

    AVAILABLE_APARTMENTS_FOR_BELL_RINGING: list[int] = [
        int(apartment_number)
        for apartment_number in os.getenv(
            "AVAILABLE_APARTMENTS_FOR_BELL_RINGING", "201,204"
        ).split(",")
    ]

    WHATSAPP_ACCESS_TOKEN: str = os.getenv("WHATSAPP_ACCESS_TOKEN")
    WHATSAPP_API_URL: str = os.getenv("WHATSAPP_API_URL")
    WHATSAPP_FINAL_NUMBER: str = os.getenv("WHATSAPP_FINAL_NUMBER")
