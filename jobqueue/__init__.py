from easydict import EasyDict as edict
from pathlib import Path
import os

from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")
REDIS_PORT = os.getenv("REDIS_PORT")

app = edict({
  'redis_host': REDIS_HOST,
  'redis_password': REDIS_PASSWORD,
  'redis_port': REDIS_PORT,
})

