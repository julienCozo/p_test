from celery import Celery
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

app = Celery('tasks', broker='pyamqp://guest@rabbit//')

@app.task
def task_example(name):

    logger.info(f"Task {name} succesful.")
    return f"Task {name} done"

app.conf.beat_schedule = {
    'periodic-task': {
        'task': 'app.task_example',
        'schedule': 5.0,
        'args': (f" {time.time() }",),
    },
}
