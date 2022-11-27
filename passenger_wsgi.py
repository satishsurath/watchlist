import sys, os
INTERP = os.path.join(os.environ['HOME'], 'watchlist', 'venv', 'bin', 'python3')

#This checks if we are in Production environment ['HOME'] == '/home/dh_5a5dek'
#If we are not in Production - then it loads the Python Path from the .env file
if os.environ['HOME'] != '/home/dh_t9c9mm':
    from dotenv import load_dotenv 
    load_dotenv()
    if (os.environ.get('pythonINTERP')):
        INTERP = os.environ.get('INTERP')


if sys.executable != INTERP:
        os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())


from flask import Flask
application = Flask(__name__)

##############################################################################################
################## Below Lines are for Hello From Passenger - First Website
@application.route('/')
def index():
    return 'Hello from Passenger'

#sys.path.append('app')
#from app import app as application

