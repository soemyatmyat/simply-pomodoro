import os 
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env')) # take environment variables from .env.

BASEDIR_APP=os.path.abspath(os.path.dirname(__file__))
SECRET_KEY=os.environ.get("SECRET_KEY") # https://flask.palletsprojects.com/en/1.1.x/api/#sessions

