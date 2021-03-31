#!/bin/sh

python manage.py migrate
python manage.py shell < createsuperuser.py
python manage.py runserver 0.0.0.0:8000