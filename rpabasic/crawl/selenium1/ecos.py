# 한국은행 경제 통계시스템 엑셀 다운로드
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# options = webdriver.ChromeOptions()
# # 브라우저 창을 띄우지 않음
# options.headless = True

browser = webdriver.Chrome()
browser.get("http://ecos.bok.or.kr")
browser.maximize_window()
time.sleep(3)

# 100대 통계지표 찾기
browser.find_element(
    By.XPATH, '//*[@id="root"]/div[5]/div/div[2]/div[4]/div[1]/div[3]/ul/li[1]/a'
).click()
time.sleep(5)

# 엑셀 다운로드 버튼 찾기
browser.find_element(By.CSS_SELECTOR, "div.exelDown.partition-right > button").click()

time.sleep(3)
browser.quit()
