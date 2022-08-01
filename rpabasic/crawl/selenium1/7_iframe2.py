from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
browser.maximize_window()

browser.get(
    "https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio"
)
time.sleep(1)

h1_element = browser.find_element(
    By.XPATH,
    '//*[@id="textareawrapper"]/div/div[6]/div[1]/div/div/div/div[5]/pre[5]/span/span[4]',
)
print(h1_element.text)

# iframe 안으로 이동
browser.switch_to.frame("iframeResult")

# 첫번째 라디오 찾은 후 클릭
browser.find_element(By.ID, "html").click()


time.sleep(3)
browser.quit()
