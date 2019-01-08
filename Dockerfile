FROM python:3.6-alpine

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ARG DJANGO_SECRET_KEY

RUN apk update
RUN apk add --no-cache jpeg-dev zlib-dev libpq #PILLOWW
RUN apk add --no-cache libxslt-dev libxml2-dev

RUN apk add --no-cache --virtual \
                       .build-deps gcc libc-dev linux-headers pkgconf git openssh py-psycopg2 postgresql-dev \
                       make gettext
# Предотвращаем неудачную компиляцию uWSGI внутри Docker, см. https://git.io/v1ve3
RUN (while true; do pip --no-cache-dir install uwsgi==2.0.14 && break; done)


WORKDIR /usr/src/app
COPY requirements.txt /usr/src/app/
COPY uwsgi.ini /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt
RUN pip install --no-cache-dir psycopg2

COPY . /usr/src/app
RUN mkdir -p /usr/src/app/static
RUN SECRET_KEY="$DJANGO_SECRET_KEY" ./manage.py collectstatic --noinput && \
    ./manage.py makemessages && \
    apk del .build-deps

EXPOSE 8000

#ENTRYPOINT ["uwsgi", "--ini", "/usr/src/app/uwsgi.ini"]
