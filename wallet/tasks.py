from celery.decorators import task,periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab

@periodic_task(run_every=(crontab(hour='*/1')), name='get_rates')
def get_fx():
	pass