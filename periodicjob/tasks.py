from celery.schedules import crontab
from celery.decorators import periodic_task
from .handlers import register_business_handler

# @periodic_task(run_every=crontab(minute="*", hour="1"), name="periodicjob.tasks.register_business_remainder")
# def register_business_remainder():
#         register_business_handler()

