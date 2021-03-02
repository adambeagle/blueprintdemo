# This is a python-dotenv file.
# It sets environment variables that allow use of the `flask run` command when working locally, to start the development server.
# In production, the app is run from Procfile, which invokes gunicorn and ignores this file.

# These are defined by Flask (see https://flask.palletsprojects.com/en/1.1.x/cli/)
FLASK_APP=wsgi
FLASK_ENV=development
FLASK_RUN_PORT=3000
#FLASK_RUN_HOST=0.0.0.0 # Uncomment to expose application to LAN
