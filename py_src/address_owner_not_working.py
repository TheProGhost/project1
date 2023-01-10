from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import requests

# opening browser in headless mode
options = Options()
options.add_argument("--headless")
sc = Service("/home/theproghost/Downloads/geckodriver-v0.31.0-linux64/geckodriver")
driver = webdriver.Firefox(service=sc,
                            options=options)

url = "https://oxt.me/address/"

addrs = "3FGKwP7XQA9Gb27if7zQGJSSynbzWLrV3p"


# driver.get(url+addrs)

reqst = requests.get(url+addrs, allow_redirects=True)

print(reqst.text)
# driver.get(reqst.text)

# element = driver.find_elements(By.XPATH, "//div/div/div/addr-header-view")

# print(element)

# for i in element:
#     print(i.text)


# driver.exit()
# driver.quit()