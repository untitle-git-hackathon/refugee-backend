FROM python:3.7

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app

RUN pip install -r requirements.txt

CMD ["python", "/app/manage.py", "runserver", "0.0.0.0:8000"]
