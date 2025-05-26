import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
 

# # Configure Selenium WebDriver
def download_video(link):
    driver.get('https://www.savethevideo.com/home')

    try:
        time.sleep(10)  # Wait for the page to load
        username_input = driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/main/section[1]/div/div[1]/div/form/input')

        # Ensure the field is focused
        username_input.click()

        # Input the link using one of the robust methods
        driver.execute_script("arguments[0].value = arguments[1];", username_input, link)
        print(f"Link sent: {link}")
        
        # Submit the form
        username_input.send_keys(Keys.RETURN)
        time.sleep(200)  # Wait for processing
    except Exception as e:
        print("Error occurred:", e)


# Example usage
video_url = "https://example.com/path/to/video.mp4"  # Replace with actual video UR
save_path = "downloaded_video.html"
# options = webdriver.ChromeOptions()
# options.add_argument("--headless")  # Optional: Run in the background
driver = webdriver.Chrome()

# Open Instagram Login Page
driver.get("https://www.instagram.com/accounts/login/")

try:
    # Wait for the login fields to appear
    wait = WebDriverWait(driver, 10)
    # time.sleep(200)
    username_input = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_input = driver.find_element(By.NAME, "password")

    # Enter login credentials
    username_input.send_keys("jayantyadav407")
    password_input.send_keys("Sweta7081")
    password_input.send_keys(Keys.RETURN)
    time.sleep(10)
    # Wait for the page to load after login
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div/div/div[3]/span/div/a/div").click()
    time.sleep(5)
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/div/div/div[1]/div/a[3]/div[1]").click()
    time.sleep(5)
    posts = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/div[2]/div[2]/div/div/div/div[1]/a/div/div[2]").click()
     
    print("test verified")
    time.sleep(5)  # Allow time for the posts to load
    posts = driver.find_elements(By.XPATH, "/html/body/div[1]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/section/main/div/div/div[3]/article/div[1]/div/div[2]/div[1]/a")
    # Scrape post data (adjust selectors as needed)
    print("last stage")
    old_height = driver.execute_script('return document.body.scrollHeight')
    count = 100
    while count>0:                                    
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        
        time.sleep(2)
        newHeight = driver.execute_script('return document.body.scrollHeight')
        print(count)
        print(old_height)
        print(newHeight)

        count = count-1
        
    time.sleep(5)

    html = driver.page_source
    with open('ajio.html','w',encoding='utf-8') as f:
        f.write(html)
    print(old_height)
except Exception as e:
    print("Error: Jai ho bharo baba", e)

finally:
    driver.quit()







