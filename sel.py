import time

import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def telebots(mess):
    requests.get(
        url=f"https://api.telegram.org/bot5082135962:AAGhUTECboqGDnU8gAtY8kK8VgWUbdjmeVc/sendMessage?chat_id=935920479&parse_mode=HTML&text={mess}")


chrome_options = Options()
# chrome_options.headless = True
chrome_options.add_argument("--no-sandbox")
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-notifications')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--disable-gpu')
chrome_options.add_argument("window-size=1280,720")

chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=chrome_options)
url = 'https://heroku.com'
driver.get(url)
print(driver.title)
telebots(driver.title)
while True:
    time.sleep(5)
    driver.get('http://youtube.com')
    telebots(driver.title)
    time.sleep(5)
    driver.get('http://python.org/downloads')
    telebots(driver.title)

