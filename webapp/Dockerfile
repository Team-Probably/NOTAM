FROM python:3.6-alpine

ENV FLASK_SECRET_KEY=trewqyuio

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 5000

CMD ["gunicorn", "--chdir", "/app", "run:app", "-b", "0.0.0.0:5000"]
