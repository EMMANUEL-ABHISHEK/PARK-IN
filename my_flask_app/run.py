# run.py

import os
from app import create_app, db  # Import your app factory and database instance
from flask_migrate import Migrate  # Import Flask-Migrate for database migrations

# Create an app instance using the default configuration
app = create_app()

# Initialize Flask-Migrate with the app and database
migrate = Migrate(app, db)

# Set the environment variables if not already set
if 'FLASK_ENV' not in os.environ:
    os.environ['FLASK_ENV'] = 'development'  # Set the environment to development

if 'SECRET_KEY' not in os.environ:
    os.environ['SECRET_KEY'] = '240b297103199d8c322f0e5dd215188ddcf3153f3ffe3304b667392ce40b1518'

if 'DATABASE_URL' not in os.environ:
    os.environ['DATABASE_URL'] = 'sqlite:///site.db'  # Set the default database URL

if __name__ == '__main__':
    # Run the Flask development server
    app.run(debug=True)
