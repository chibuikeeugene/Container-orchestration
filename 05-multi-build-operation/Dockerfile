#----------stage:builder-----------
FROM python:3.13-slim AS builder

WORKDIR /build

RUN python -m venv /opt/venv

ENV PATH="/opt/venv/bin:$PATH"

COPY requirements.txt .

RUN python -m pip install --no-cache-dir -r requirements.txt

#---------stage:runtime-----------
FROM python:3.13-slim AS runtime

ENV PYTHONUNBUFFERED=1 \
PYTHONDONOTWRITEBYTECODE=1 \
PATH="/opt/venv/bin:$PATH"

RUN useradd --create-home --uid 10001 appuser

WORKDIR /app

COPY --from=builder /opt/venv /opt/venv

COPY --chown=appuser:appuser app.py .

USER appuser

EXPOSE 8001

HEALTHCHECK \
 --interval=30s \
 --timeout=30s \
 --start-period=5s \
 --retries=3 \
 CMD python -c "import urllib.request; urllib.request.urlopen('http://0.0.0.0:8001/health', timeout=20)"

CMD [ "uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001" ]