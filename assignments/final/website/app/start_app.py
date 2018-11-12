import os

from app import app

from app.routes import *

if __name__ == '__main__':
    os.environ['FLASK_ENV'] = 'development'  # Enable auto-restart.

    app.run()
