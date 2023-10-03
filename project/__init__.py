from flask import Flask
from .utils import make_celery
from .tasks import *

def create_app():
    app = Flask(__name__)
    app.config["CELERY_CONFIG"] = {
        "broker_url": "redis://127.0.0.1:6379/0", 
        "result_backend": "redis://127.0.0.1:6379/0", 
    }

    celery = make_celery(app)
    celery.set_default()
    

    return app, celery
