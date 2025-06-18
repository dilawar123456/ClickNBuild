import sys
import os

# Add your project directory to the sys.path
project_home = '/home/Dilawar123'
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# Set environment variable for Flask
os.environ['FLASK_APP'] = 'run.py'

# Import your Flask app
from app import create_app
application = create_app() 