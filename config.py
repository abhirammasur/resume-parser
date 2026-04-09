import os

class Config:
    SECRET_KEY = 'secretkey'
    UPLOAD_FOLDER = 'uploads'
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
