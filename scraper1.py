import time
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


service = Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service = service, options = options)

url = "https://www.crisisgroup.org/crisiswatch/database?location%5B%5D=57&location%5B%5D=62&location%5B%5D=70&location%5B%5D=71&location%5B%5D=58&crisis_state=&created=-3+months&from_month=1&from_year=2025&to_month=1&to_year=2025"

driver.get(url)

time.sleep(5)

lst = []

entries = driver.find_elements(By.CLASS_NAME, "c-crisiswatch-entry")


for entry in entries:

    country_name = entry.find_element(By.TAG_NAME, "h3").text.strip()

    month_year = entry.find_element(By.TAG_NAME, "time").text.strip()

    title_element = entry.find_element(By.CSS_SELECTOR, ".o-crisis-states__detail p strong")
    title = title_element.text.strip()



    paragraphs = entry.find_elements(By.CSS_SELECTOR, ".o-crisis-states__detail p")
    paragraph_text = " ".join([p.text.strip() for p in paragraphs])



    lst.append({
        "Country": country_name,
        "Month_Year": month_year,
        "Title": title,
        "Paragraph": paragraph_text
    })


driver.quit()


df = pd.DataFrame(lst)

df.to_csv("crisis_data.csv", index = False, encoding = "utf-8-sig")

print("Success")

