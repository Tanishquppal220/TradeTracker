# After logging into PythonAnywhere, open a Bash console and run these commands:

# Create a directory for your application
mkdir -p ~/TradeTracker

# If using Git:
# git clone https://github.com/yourusername/TradeTracker.git ~/TradeTracker

# If using direct upload, upload your ZIP file through the PythonAnywhere Files tab
# Then in Bash console:
# unzip ~/your_uploaded_file.zip -d ~/TradeTracker

# Set up a virtual environment
python -m venv ~/TradeTracker/venv

# Activate the virtual environment
source ~/TradeTracker/venv/bin/activate

# Install your requirements
pip install -r ~/TradeTracker/requirements.txt

# Additionally, you might need these PythonAnywhere-specific packages
pip install mysqlclient

# If you want to keep using SQLite (which is fine for smaller applications):
# No additional steps needed, just make sure your app points to the correct database path
