import os
from celery.schedules import crontab
from jobqueue import app

CELERY_TASK_SERIALIZER = 'json'
BROKER_URL = os.getenv('REDIS_URL', f'redis://h:{app.redis_password}@{app.redis_host}:{app.redis_port}') 
CELERY_ACCEPT_CONTENT = ['json']

CELERY_IMPORTS = ('jobqueue.tasks')

CELERY_TASK_RESULT_EXPIRES = 30
CELERY_TIMEZONE = 'Asia/Ho_Chi_Minh'

CELERY_ACCEPT_CONTENT = ['json', 'msgpack', 'yaml']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

CELERYBEAT_SCHEDULE = {
  # 'auto-crawl-data-by-hour': {
  #   'task': 'app.tasks.crawl_data_every_hour',
  #   'schedule': crontab(hour="*"),
  # },
}
