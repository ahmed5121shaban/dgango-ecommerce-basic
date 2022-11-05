
from celery import shared_task
import time


@shared_task
def task_celery(request,n):
    time.sleep(n)
    print('Ahmed Shaban')

