import redis
from app.core.config import settings

REDIS_URL = settings.REDIS_URL
if not REDIS_URL:
    raise ValueError("REDIS_URL must be set in environment or in app.core.config.Settings")

redis_client = redis.StrictRedis.from_url(REDIS_URL, decode_responses=True)


def get_cached_prediction(key: str):
    value = redis_client.get(key)
    return eval(value) if value else None


def set_cached_prediction(key: str, value: dict):
    redis_client.set(key, str(value))