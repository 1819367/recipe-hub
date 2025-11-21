# server/config.py
import os
import logging

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'default_secret')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'  # Local dev fallback

class ProductionConfig(Config):
    DEBUG = False
    uri = os.environ.get('DATABASE_URL')
    if uri:
        SQLALCHEMY_DATABASE_URI = uri.replace('postgres://', 'postgresql://')
    else:
        logging.warning("DATABASE_URL not set; using SQLite fallback.")
        SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'
