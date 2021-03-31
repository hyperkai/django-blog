#!/bin/sh

python manage.py migrate
python manage.py shell < createsuperuser.py
gunicorn -w 3 django_project.wsgi -b 0.0.0.0:8000