from celery.decorators import task,periodic_task
from celery.utils.log import get_task_logger
from celery.task.schedules import crontab
from wallet.utils import get_fx

logger=get_task_logger(__name__)

@periodic_task(run_every=(crontab(minute='*/2')), name='get_rates',ignore_result=True)
def task_get_fx():
	""" 
	Gets the forex rates once an hour

	"""

	get_fx()
	logger.info("Got Forex Rates")
	