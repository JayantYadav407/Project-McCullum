from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open the webpage
driver.get("https://rocketlaunch.org/rocket-launch-recap")  # Replace with the actual URL
time.sleep(5)
 
print("ho gyaaaaaaaaaaaaa1")
i = 1966 
while i<2025:
    try:
        # Scroll into view if necessary
        driver.execute_script("window.scrollBy(0, 50);")
        time.sleep(2)  # Pause to see the effect
        link = driver.find_element(by=By.ID ,value=str(i))
        link.find_element(By.TAG_NAME, "a").click()
        print(i)

        # Scroll up by a specific height (e.g., 500 pixels)
        driver.execute_script("window.scrollBy(0, -50);")
        time.sleep(2) 
        time.sleep(6)
        html = driver.page_source
        time.sleep(2) 
        with open(f'Annual_Recape/{i}_page.html','w',encoding='UTF8-') as f:
            f.write(html)
        driver.back()
        time.sleep(2)
        i = i+1
    except Exception as e:
        print(f"Error clicking link box {e}")

# Close the WebDriver
driver.quit()
