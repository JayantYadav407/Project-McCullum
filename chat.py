from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time

# Setup WebDriver
driver = webdriver.Chrome()

# YouTube video URL with live chat replay
video_url = "https://www.youtube.com/watch?v=2PnbFqm1vUY&t=1359s"
driver.get(video_url)

# Wait for the page to load
time.sleep(10)

# Locate and switch to the live chat iframe
try:
    chat_frame = driver.find_element(By.CSS_SELECTOR, "iframe#chatframe")
    driver.switch_to.frame(chat_frame)
except Exception as e:
    print("Failed to locate or switch to the live chat iframe:", e)
    driver.quit()
    exit()

# Initialize list to store messages
messages = []

# Scroll and collect messages
print("Scraping live chat messages...")
try:
    for _ in range(50):  # Adjust the range for more messages
        chat_items = driver.find_elements(By.CSS_SELECTOR, "yt-live-chat-text-message-renderer")
        for item in chat_items:
            try:
                author = item.find_element(By.CSS_SELECTOR, "#author-name").text
                message = item.find_element(By.CSS_SELECTOR, "#message").text
                messages.append({"Author": author, "Message": message})
            except Exception as e:
                # Skip if any element is missing
                continue
        driver.execute_script("window.scrollBy(0, 500);")  # Scroll down
        time.sleep(2)
except Exception as e:
    print("Error while scraping chat:", e)

# Save collected messages to an Excel file
if messages:
    df = pd.DataFrame(messages)
    output_file = "YouTube_Live_Chat.xlsx"
    df.to_excel(output_file, index=False)
    print(f"Chat messages saved to {output_file}")
else:
    print("No chat messages were scraped.")

# Close the WebDriver
driver.quit()
