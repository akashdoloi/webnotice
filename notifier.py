import time
import requests
from bs4 import BeautifulSoup
from telegram import Bot

# === Configuration ===
BOT_TOKEN = "7551042371:AAEfljTJYJ1kA2rL2SBenug5uhbvBfHv0UQ"
CHAT_ID = 5095679376
CHECK_INTERVAL = 60  # seconds

bot = Bot(token=BOT_TOKEN)

# === Last seen notices tracker ===
last_notices = {}

# === Website-specific scraping logic ===

def fetch_ssc_notice():
    """
    Scrapes the latest notification title and link from ssc.nic.in
    """
    url = "https://ssc.gov.in/"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        # SSC notice block (adjusted to work dynamically)
        latest = soup.select_one("#latest-news marquee a")
        if latest:
            title = latest.text.strip()
            link = "https://ssc.gov.in" + latest['href']
            return "SSC", title, link
    except Exception as e:
        return "SSC", None, f"Error fetching SSC notice: {str(e)}"
    return "SSC", None, None

# === Add more fetchers here ===

def fetch_college_notice():
    """
    Template: Scrape a college/university website
    Replace URL and selectors based on actual site
    """
    url = "https://makautwb.ac.in/"
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")
        
        latest = soup.select_one(".notice-item a")  # Replace with actual selector
        if latest:
            title = latest.text.strip()
            link = latest.get("href")
            if not link.startswith("http"):
                link = url + link
            return "College", title, link
    except Exception as e:
        return "College", None, f"Error fetching college notice: {str(e)}"
    return "College", None, None

# === Add more websites by defining new fetch_xxx functions ===

fetch_functions = [fetch_ssc_notice, fetch_college_notice]

# === Main Monitoring Loop ===

def main():
    global last_notices

    while True:
        for fetch_func in fetch_functions:
            source, title, link = fetch_func()

            if title and last_notices.get(source) != title:
                message = f"**New {source} Notification:**\n{title}\n{link}"
                bot.send_message(chat_id=CHAT_ID, text=message)
                last_notices[source] = title

        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    main()