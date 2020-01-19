from celery import Celery


app = Celery()
app.config_from_object("jobqueue.settings")

@app.task(name='jobqueue.tasks.crawl_data_every_hour')
def crawl_data_every_hour():
    pass