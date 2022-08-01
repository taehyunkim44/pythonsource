# 다나와 상품 자동화
from math import prod
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from bs4 import BeautifulSoup

from openpyxl import Workbook
from openpyxl.drawing.image import Image

import requests
from io import BytesIO

wb = Workbook()
ws = wb.active
ws.title = "애플"
ws.column_dimensions['B'].width = 55
ws.column_dimensions['C'].width = 20
ws.column_dimensions['D'].width = 80
ws.column_dimensions['E'].width = 10

# 타이틀 행 추가
ws.append(["번호","제품명","가격","이미지경로","이미지"])


browser = webdriver.Chrome()
browser.get("http://prod.danawa.com/list/?cate=112758&15main_11_02")
browser.maximize_window()

# 제조사 더보기 클릭
WebDriverWait(browser, 3).until(EC.presence_of_element_located((By.XPATH, '//*[@id="dlMaker_simple"]/dd/div[2]/button[1]'))).click()
# 애플 클릭
browser.find_element(By.XPATH,'//*[@id="selectMaker_simple_priceCompare_A"]/li[17]/label').click()

# 제품 목록이 화면에  로딩되도록 대기
time.sleep(5)


# print(browser.page_source)


# 상품 정보 추출 - 상품명, 가격(첫번째), 이미지 src

# 상품 목록 리스트 가져오기
# product_list = browser.find_elements(By.CSS_SELECTOR, "div.main_prodlist_list li:not(.prod_ad_item):not(.product-pot)")



# print(product_list)

# 현재 페이지/ 크롤링할 페이지 수
cur_page, target_crawl_num = 1, 6 

# 번호 출력
idx = 1


while cur_page <= target_crawl_num:

    soup = BeautifulSoup(browser.page_source, "lxml")

    product_list = soup.select(
    "div.main_prodlist_list > ul > li:not(.prod_ad_item):not(.product-pot)"
    )

    # 현재 페이지 출력
    print("=========== Current Page : {}".format(cur_page))

    # 상품 정보 출력
    for product in product_list:

        # 제품명
        # product_name = product.find_element(By.CSS_SELECTOR,"p > a").text.strip()
        product_name = product.select_one("p > a").text.strip()

        # 가격
        # product_price = product.find_element(By.CSS_SELECTOR, "p.price_sect > a").text.strip()
        product_price = product.select_one("p.price_sect > a").text.strip()

        # 이미지 경로
        # product_image = product.find_element(By.CSS_SELECTOR,".thumb_image img")
        product_image = product.select_one(".thumb_image img")  

        # if product_image.get_attribute("data-original"):
        #     product_image = product_image.get_attribute("data-original")
        # else:
        #     product_image = product_image.get_attribute("src")

        if product_image.get("data-original"):
            product_image = product_image.get("data-original")
        else:
            product_image = product_image.get("src")

        if "http:" not in product_image:
            product_image = "http:"+ product_image

        print(idx,product_name,product_price,product_image)
        #  상품 정보 엑셀 삽입
        ws.append([idx,product_name,product_price,product_image])
        # 이미지 다운로드 받아서 엑셀 삽입
        res = requests.get(product_image)
        img_save = BytesIO(res.content)
        idx += 1

        img = Image(img_save)
        img.width = 30
        img.height = 20
        ws.add_image(img, "E" + str(idx)) # E2 셀부터 삽입 시작


    print()
    browser.save_screenshot("./rpabasic/crawl/download/target_page{}.png".format(cur_page))

    # 현재 페이지 번호 변경
    cur_page += 1

    if cur_page > target_crawl_num:
        print('크롤링 성공')
        break

    # 다음 페이지 클릭
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(2)
    # #productListArea > div.prod_num_nav > div > div > a:nth-child(3)
    WebDriverWait(browser,2).until(EC.presence_of_element_located((By.CSS_SELECTOR,"div.number_wrap > a:nth-child({})".format(cur_page)))).click()

    # soup 삭제
    del soup

    # 다음 페이지 로딩될 때까지 기다리기
    time.sleep(3)

wb.save("./rpabasic/crawl/download/danawa.xlsx")
wb.close()
    
time.sleep(3)
browser.quit()