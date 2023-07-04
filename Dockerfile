FROM python:3.11

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip
RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]