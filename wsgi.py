import sys
import os

# Add your project directory to the sys.path
path = '/home/YOUR_PYTHONANYWHERE_USERNAME/TradeTracker'
if path not in sys.path:
    sys.path.insert(0, path)

# Import your Flask app
from app import app as application
