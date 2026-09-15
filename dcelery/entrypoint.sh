#!/bin/ash


echo "Applying migrations..."
python manage.py migrate

exec "$@" # exec the CMD from the Dockerfile