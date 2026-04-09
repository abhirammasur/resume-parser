class Config:
    SECRET_KEY = 'secretkey'
    UPLOAD_FOLDER = 'uploads'
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost/resume_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
