# gmarket 접속하고 상품명 입력한 후 결과 페이지 이동
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("https://www.gmarket.co.kr/")
browser.maximize_window()

# 검색창 찾기
element = browser.find_element(By.NAME, "keyword")
element.send_keys("마스크")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()
