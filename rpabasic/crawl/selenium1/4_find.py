from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.get("http://www.daum.net")
browser.maximize_window()

# 원하는 요소 찾기
element = browser.find_element(By.NAME,"q")
# print(element) #<selenium.webdriver.remote.webelement.WebElement (session="0285231864f135d7e3a5ad7861c6d18b", element="ed3f9f14-30c5-428a-b33c-b693f9d25fe4")>                                                                                                                                                                                                                                                                               
# 검색어 넣기
element.send_keys("아이폰")
element.send_keys(Keys.ENTER)

time.sleep(3)
browser.quit()