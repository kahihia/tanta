from celery.task.schedules import crontab
from celery.decorators import periodic_task,task
from .celery import app
from __future__ import absolute_import,unicode_literals


@task
def add(x,y):
	return x + y
@task
def mul(x,y):
	return x * y

@periodic_task(run_every=(crontab(minute='*/15')), name="some_task", ignore_result=True)
def some_task():
    # do something
