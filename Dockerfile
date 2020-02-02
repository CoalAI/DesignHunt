FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
CMD python manage.py migrate && gunicorn -b 0.0.0.0:8000 DesignHunt.wsgi
