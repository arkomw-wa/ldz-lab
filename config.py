import os

class Config:
    SECRET_KEY = 'your_secret_key'
    # Use the Azure PostgreSQL connection string
    SQLALCHEMY_DATABASE_URI = (
        "postgresql+psycopg2://endpointdb:{P@ssw0rd}@testdb01.postgres.database.azure.com:5432/ldz_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
