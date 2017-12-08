FROM python:2.7-slim

WORKDIR /app

ADD ./stress.py /app

CMD ["python", "stress.py"]