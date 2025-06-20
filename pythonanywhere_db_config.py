# Modified database configuration for PythonAnywhere
# You might want to replace the existing database configuration in your app.py
# with something like this:

import os
from pathlib import Path

# Get the directory where app.py is located
BASE_DIR = Path(__file__).resolve().parent

# Configure CS50 Library to use SQLite database
db = SQL(f"sqlite:///{BASE_DIR}/New_Database.db")
