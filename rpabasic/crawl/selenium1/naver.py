# 네이버 항공권 자동화
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

browser = webdriver.Chrome()
browser.get("https://flight.naver.com/")
browser.maximize_window()
time.sleep(1)


try:
    # 도착 클릭
    WebDriverWait(browser, 1).until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.tabContent_routes__laamB > button:nth-child(2)")
        )
    ).click()

    # browser.find_element(
    #     By.CSS_SELECTOR, "div.tabContent_routes__laamB > button:nth-child(2)"
    # ).click()

    time.sleep(1)

    # 국내 클릭
    browser.find_element(
        By.XPATH, '//*[@id="__next"]/div/div[1]/div[9]/div[2]/section/section/button[1]'
    ).click()

    time.sleep(3)

    # 제주 클릭
    browser.find_element(
        By.CSS_SELECTOR,
        "div.autocomplete_list__de1dI > button:nth-child(2) > span",
    ).click()

    # 가는날 클릭
    browser.find_element(
        By.CSS_SELECTOR, "div.tabContent_options__KwvIB > button"
    ).click()
    time.sleep(2)

    # 가는날짜 클릭 - 6월 27일
    browser.find_element(
        By.CSS_SELECTOR,
        "div.awesome-calendar > div:nth-child(2) tr:nth-child(5) > td:nth-child(2) > button",
    ).click()

    time.sleep(2)

    # 오는날짜 클릭 - 6월 30일
    browser.find_element(
        By.CSS_SELECTOR,
        "div.awesome-calendar > div:nth-child(2) tr:nth-child(5) > td:nth-child(5) > button",
    ).click()

    # 항공권 검색 클릭
    browser.find_element(
        By.CSS_SELECTOR, "div.main_searchbox__3vrV3 > div > div > button"
    ).click()

    # 항공권 검색 결과 출력 (항공사)
    airline = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located(
            (
                By.CSS_SELECTOR,
                "div.domestic_schedule__1Whiq > div > div.heading > div.airline",
            )
        )
    )
    print(airline.text)

except Exception as e:
    print(e)


time.sleep(3)
browser.quit()
