import sys, os
from dotenv import load_dotenv 
load_dotenv()
# INTERP = os.path.join(os.environ['HOME'], 'watchlist', 'venv', 'bin', 'python3')
INTERP = os.environ.get("pythonINTERP")
if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())
from flask import Flask
application = Flask(__name__)
@application.route('/')
def index():
    return 'Hello from Passenger'

