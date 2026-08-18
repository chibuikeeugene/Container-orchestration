import os
import psycopg
from fastapi import FastAPI

app = FastAPI()

# get environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "")

# get application  info
@app.get("/")
def root():
    """application root"""
    return {"message": "fastapi docker compose application"}

# get application status
@app.get("/health")
def health():
    """check application health status"""
    return {"status": "ok"}

# get database user and name
@app.get("/database")
def database():
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute("SELECT current_database(), current_user")
            database_name, user_name = cursor.fetchone()

    return {
        "database name": database_name,
        "user": user_name
    }

# send information to database
@app.post("/visits")
def add_visits():
    """add new visitor data to database"""
    with psycopg.connect(DATABASE_URL) as connection:
        with connection.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS visits (
                    id SERIAL PRIMARY KEY,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
                """
            )
            cursor.execute(
                "INSERT INTO visits DEFAULT VALUES"
            )

            cursor.execute(
                "SELECT count(*) FROM visits"
            )

            result = cursor.fetchone()[0]

    return {
        "visits": result
    }