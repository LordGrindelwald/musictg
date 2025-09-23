import os
import threading
from flask import Flask
from TgMusic.__main__ import main as start_bot

# Create a Flask app
app = Flask(__name__)

# Define a simple route
@app.route('/')
def hello_world():
    return 'The bot is running!'

# Function to run the bot in a separate thread
def run_bot():
    start_bot()

# Start the bot in a background thread
if __name__ == "__main__":
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()
    # Get the port from the environment variable, default to 10000
    port = int(os.environ.get('PORT', 10000))
    # Run the Flask app
    app.run(host='0.0.0.0', port=port)
