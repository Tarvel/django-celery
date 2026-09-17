from .celery import app as celery_app

__all__ = ('celery_app',) 
# this line is used to define the public interface of the module
# It specifies that when you import * from this module (folder), only the celery_app object will be imported
# This is a way to control what is exposed to other modules and prevent unnecessary imports
