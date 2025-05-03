#!/bin/sh
echo "running migrations"
python manage.py migrate
echo "starting server....."
python manage.py
runserver 0.0.0:8000