from flask import Flask
from threading import Thread
import notifier  # Your notifier.py script

app = Flask(__name__)

@app.route('/')
def home():
    return "Telegram bot is running!"

def run_bot():
    notifier.main()

if __name__ == '__main__':
    # Run the Telegram bot in a background thread
    Thread(target=run_bot).start()

    # Start Flask server to keep Render happy
    app.run(host='0.0.0.0', port=10000)
