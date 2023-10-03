from celery import shared_task, current_app as celery_app
import time

@shared_task
def add(x, y):
    time.sleep(5) 
    return x + y


@shared_task
def sub(x, y):
    return x - y
