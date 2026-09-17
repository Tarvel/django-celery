import os
from celery import Celery


# used to load the settings.py file of the django project. This is necessary for Celery to access the Django settings and configurations
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dcelery.settings') 

# initialize a new Celery application instance with the name 'dcelery'. This name is used to identify the Celery application
app = Celery('dcelery')

# load the celery configs from the django settings file, using CELERY as name space (anything that starts with CELERY_ in the settings.py file will be used as a celery config)
app.config_from_object('django.conf:settings', namespace='CELERY')

@app.task
def add_numbers():
    return


app.autodiscover_tasks() # finds all the tasks located in task.py of the installed apps (in django settings.py file) and registers them with the Celery application. This allows Celery to know about all the tasks defined in the project and be able to execute them when requested.
