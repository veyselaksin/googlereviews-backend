from django.core.management import call_command
# from celery.schedules import crontab
# from celery.decorators import periodic_task
from .handlers import register_business_handler
import os

# @periodic_task(run_every=crontab(minute="0", hour="9"), name="periodicjob.tasks.register_business_remainder")
# def register_business_remainder():
#         register_business_handler()

