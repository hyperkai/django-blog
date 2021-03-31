FROM python:3.10.0a6-alpine3.13

ENV PYTHONUNBUFFERED 1

WORKDIR /app

ADD . .

RUN apk add --no-cache gcc musl-dev python3-dev \ 
    libffi-dev openssl-dev cargo postgresql-dev \
    jpeg-dev zlib-dev
RUN pip install -r requirements.txt
CMD sh start.sh

#CMD sh -c "python manage.py migrate && \
#    DJANGO_SUPERUSER_USERNAME=admin \
#    DJANGO_SUPERUSER_EMAIL=admin@admin.com \
#    DJANGO_SUPERUSER_PASSWORD=admin \
#    python manage.py createsuperuser --noinput && \
#    python manage.py runserver 0.0.0.0:8000"