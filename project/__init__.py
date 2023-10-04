from flask import Flask
from .utils import make_celery
from .tasks import *

def create_app():
    app = Flask(__name__)
    app.config["CELERY_CONFIG"] = {
        "broker_url": "redis://celery-redis:6379/0", 
        "result_backend": "redis://celery-redis:6379/0",
        "beat_schedule": {
            "scheduled-task":{
                "task" : "project.tasks.scheduled_task",
                "schedule" : 15
            }
        } 
    }

    celery = make_celery(app)
    celery.set_default()
    

    return app, celery
