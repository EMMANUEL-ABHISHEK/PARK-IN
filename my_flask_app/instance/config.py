# instance/config.py

import os

# Get the secret key from the environment variable or use a default value
SECRET_KEY = os.environ.get('SECRET_KEY', '240b297103199d8c322f0e5dd215188ddcf3153f3ffe3304b667392ce40b1518')

# Configure the database URI (for example, using SQLite)
SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', 'sqlite:///site.db')

# Track modifications flag (set to False to save resources)
SQLALCHEMY_TRACK_MODIFICATIONS = False
