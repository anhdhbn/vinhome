from easydict import EasyDict as edict
from pathlib import Path
import os

from dotenv import load_dotenv
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path, verbose=True)


app = edict({
  'redis_host': REDIS_HOST,
  'redis_password': REDIS_PASSWORD,
  'redis_port': REDIS_PORT,
})