import os
from dotenv import load_dotenv

load_dotenv()  # Încarcă variabilele de mediu din fișierul .env

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'  # Baza de date SQLite temporară pentru testare
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY")
    JWT_EXPIRY_MINUTES = 60
