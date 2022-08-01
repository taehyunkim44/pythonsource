from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get("https://www.danawa.com/")
time.sleep(1)

# 로그인 버튼 찾기
login = browser.find_element(By.CLASS_NAME, "btn_user--login")
login.click()
time.sleep(1)

# 아이디 입력 찾기
userid = browser.find_element(By.ID, "danawa-member-login-input-id")
userid.clear()
userid.send_keys("아이디")

# 비밀번호 입력 찾기
password = browser.find_element(By.ID, "danawa-member-login-input-pwd")
password.clear()
password.send_keys("본인비밀번호")
password.send_keys(Keys.ENTER)


time.sleep(3)
browser.quit()
