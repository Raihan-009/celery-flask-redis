from celery import shared_task
import time

@shared_task
def add(x, y):
    time.sleep(5) 
    return x + y


@shared_task
def sub(x, y):
    return x - y

@shared_task
def mul(x, y):
    return x * y

@shared_task
def scheduled_task():
    print("Periodic task is happening")