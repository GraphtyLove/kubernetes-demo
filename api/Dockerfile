FROM python:3.1-alpine

RUN mkdir -p /app
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "api.py"]