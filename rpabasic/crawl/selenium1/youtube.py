# 검색어 넣고 검색결과 출력
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.ChromeOptions()
# 브라우저 창을 띄우지 않음
options.headless = True
browser = webdriver.Chrome(options=options)

browser.get("https://www.youtube.com/")
browser.maximize_window()

time.sleep(2)

element = browser.find_element(By.NAME, "search_query")
element.send_keys("아이유")
element.send_keys(Keys.ENTER)
time.sleep(2)

# 검색 결과 출력
titles = browser.find_elements(By.TAG_NAME, "h3")
for title in titles:
    print(title.text)

time.sleep(3)
browser.quit()
