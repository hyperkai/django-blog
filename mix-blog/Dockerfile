FROM ubuntu:20.04

WORKDIR /blog

ADD . .

ARG DEBIAN_FRONTEND=noninteractive
#RUN apt-get update && apt-get install -y software-properties-common \
RUN apt-get update && apt-get install -y python-is-python3=3.8.2-4 \
python3-pip libpq-dev python3-testresources gunicorn nginx

ENV PYTHONUNBUFFERED 1

RUN pip3 install --target=/usr/local/lib/python3.8/dist-packages -r requirements.txt
RUN python3 manage.py migrate
RUN python3 manage.py shell < createsuperuser.py

COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf

CMD gunicorn -w 3 -b unix:/gunicorn.sock django_project.wsgi -D && nginx -g "daemon off;"

#CMD sh -c "python manage.py migrate && \
#    DJANGO_SUPERUSER_USERNAME=admin \
#    DJANGO_SUPERUSER_EMAIL=admin@admin.com \
#    DJANGO_SUPERUSER_PASSWORD=admin \
#    python manage.py createsuperuser --noinput && \
#    python manage.py runserver 0.0.0.0:8000"

