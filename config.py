import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your_default_secret_key'
    MONGODB_SETTINGS = {
        'db': 'assetdb',
        'host': 'localhost',
        'port': 27017
    }
