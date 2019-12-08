FROM python:3.6

RUN mkdir -p /opt/services/djangoapp/src
WORKDIR /opt/services/djangoapp/src

COPY requirements.txt /opt/services/djangoapp/src/
RUN pip install -r requirements.txt

COPY . /opt/services/djangoapp/src

EXPOSE 8000

RUN adduser --disabled-password --gecos '' myuser

CMD ["gunicorn", "--chdir", "crawler", "--bind", ":8000", "crawler.wsgi:application"]
