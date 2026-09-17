## LESSONS

- Django -> Redis -> Celery -> Database

- Celery is used to handle background tasks in Python applications. It allows you to run tasks asynchronously, meaning that they can be executed in the background without blocking the main application flow. This is useful for tasks that take a long time to complete, such as sending emails, processing files, or making API calls

- Celery requires a message broker (like RabbitMQ or Redis) to manage the task queue. The broker acts as an intermediary between the main application and the workers, making sure that tasks are delivered and executed properly. You need to configure Celery with the appropriate broker settings in your application

- <function>.delay() in celery adds the function (task) to the queue to be executed asynchronously by a worker. When you call <function>.delay(), it serializes the function call and sends it to the message broker, which then distributes it to available workers for execution. This allows you to offload time-consuming tasks from the main application thread, improving responsiveness and scalability

- we need to define a Celery application instance in our Django project. This is typically done in a separate file (e.g., celery.py) where we configure the Celery settings, including the broker URL, result backend, and any other necessary configurations. The Celery application instance is then imported and used to define tasks and manage the task queue

- also in `__init__.py` in the same directory as the celery.py file, we need to import the Celery application instance. This ensures that the Celery application is initialized when the Django project starts, allowing tasks to be registered and executed properly. By importing the Celery instance in `__init__.py`, we make it available throughout the Django project, enabling us to define and execute tasks from any part of the application
