from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

Link = "https://listen-assistent.netlify.app/" # Site for speech to text which i've hosted

browser_options = Options()
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.142.86 Safari/537.36"
browser_options.add_argument(f'user-agent={user_agent}')
browser_options.add_argument("--use-fake-ui-for-media-stream")
browser_options.add_argument("--use-fake-device-for-media-stream")
browser_options.add_argument("--headless")  # Use headless mode
browser_options.add_argument("--no-sandbox")  # Bypass OS security model
browser_options.add_argument("--disable-dev-shm-usage")  # Overcome limited resource problems
browser_options.add_argument("--remote-debugging-port=9222")

service = Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=service, options=browser_options)
driver.get(Link)

# Using selenium to perform speech to text
def Listen():
    driver.find_element(by=By.ID, value="start").click()
    print("\n\nListening...\n")
    while True:
        try:
            Text = driver.find_element(by=By.ID, value="output").text
            if Text:
                driver.find_element(by=By.ID, value="end").click()
                return Text
            else:
                sleep(0.333)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print("An error occurred:", e)
