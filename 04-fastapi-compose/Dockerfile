FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1 \
PYTHONDONOTWRITEBYTECODE=1

WORKDIR /app

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

RUN useradd --create-home --uid 10001 appuser

COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 8000

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000" ]