FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install -r requirements.txt

COPY client.py .

CMD [ "python", "client.py" ]