import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'sua_chave_aqui')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI', 'sqlite:///database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
