FROM python:3.12-alpine

WORKDIR /usr/src/app

# Prevent Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1 
# ensures python output is sent straight to terminal (e.g. your container log) without being first buffered and that you can see what your code is doing in real time.
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip

COPY ./requirements.txt /usr/src/app/requirements.txt

RUN pip install -r requirements.txt

COPY ./entrypoint.sh /usr/src/app/entrypoint.sh

COPY . /usr/src/app/

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]