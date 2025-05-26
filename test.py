import time
from telegram import Bot

# === Replace with your actual bot token and chat ID ===
BOT_TOKEN = "7551042371:AAEfljTJYJ1kA2rL2SBenug5uhbvBfHv0UQ"
CHAT_ID = 5095679376

# Initialize bot
bot = Bot(token=BOT_TOKEN)

# Simulate notice tracking
last_notice = None

def fetch_mock_notice():
    """
    Simulates fetching a new notice every time the script runs.
    Use this to test Telegram messaging.
    """
    import random
    mock_notice_id = random.randint(1000, 9999)
    title = f"Mock Notice #{mock_notice_id}"
    link = "https://example.com/notice"
    return title, link

def main():
    global last_notice

    while True:
        title, link = fetch_mock_notice()
        if title != last_notice:
            message = f"**New Mock Notification:**\n{title}\n{link}"
            print("Sending message:", message)
            try:
                bot.send_message(chat_id=CHAT_ID, text=message)
                last_notice = title
            except Exception as e:
                print("Error sending message:", str(e))

        time.sleep(10)  # Wait 10 seconds before sending another (for testing)

if __name__ == "__main__":
    main()