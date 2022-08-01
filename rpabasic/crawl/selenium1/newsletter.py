# 네이버에서 뉴스 링크 추출하여 가입자에게 전송

from requests import request
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

import requests

import pyperclip

browser = webdriver.Chrome()
browser.get("https://www.naver.com")
browser.maximize_window()

# 새창 띄우기
browser.execute_script('window.open("http://www.daum.net")')

# 브라우저2개 리스트로 다루기
tabs = browser.window_handles # tabs[0] : naver, tab[1] : daum

# 첫번째 탭 선택
browser.switch_to.window(tabs[0])

# 검색어 넣기
keyword = "RPA 파이썬"
browser.find_element(By.NAME, "query").send_keys(keyword)

# 검색버튼 클릭
browser.find_element(By.ID, "search_btn").click()

# 결과 기다리기
time.sleep(2)

# 뉴스 메뉴 클릭
browser.find_element(By.XPATH,'//*[@id="lnb"]/div[1]/div/ul/li[8]').click()
time.sleep(1)

# 최신순 클릭
browser.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

# 조회일 기준으로 뉴스 건수 가져오기
client_id = "_lfO7lk3pV4tTMFHiBzb"
client_secret = "_ERfhzVqcL"

url = "https://openapi.naver.com/v1/search/news.json"

headers = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret": client_secret}
param = {"query":keyword}
res = requests.get(url,headers=headers, params=param)
result = res.json()
# print(result)

# 뉴스 총 건수
new_total_cnt = result.get("total") # result['total']

# 뉴스 총 건수를 파일 저장
# 1) 기존 뉴스 건수를 읽어와서 변수에 담기
path = "./rpabasic/crawl/selenium1/totalCnt.txt"
with open(path,"r") as f :
    old_total_cnt = int(f.readline())

# 2) new_total_cnt 와 기존뉴스건수 비교 => 지난 뉴스 건수와 차이 구하기(new_add_cnt)
# 147 - 0
if new_total_cnt > old_total_cnt:
    new_add_cnt  = new_total_cnt - old_total_cnt
    # 3) new_total_cnt를 totalCnt.txt 기록
    with open(path,"w") as f:
        f.write(str(new_total_cnt))
else:
    new_add_cnt = 0

# 페이지 수 지정
if new_add_cnt == 0:
    page_cnt = 0
else:
    page_cnt = new_add_cnt // 10 + 1

start, num = 1, 1
result = ""

if page_cnt > 0:
    for i in range(page_cnt):

        start = start + (i * 10)

        url = "https://search.naver.com/search.naver?where=news&query=rpa%20%ED%8C%8C%EC%9D%B4%EC%8D%AC"
        url += "&sm=tab_opt&sort=1&photo=0&field=0&pd=0&ds=&de=&docid=&related=0"
        url += "mynews=0&office_type=0&office_section_code=0&news_office_checked="
        url += "&nso=so%3Add%2Cp%3Aall&is_sug_officeid=0&start="+str(start)

        browser.get(url)

        # 뉴스 크롤링
        # 뉴스제목, 매체, 등록일, 원문 주소
        news_area = browser.find_elements(By.CLASS_NAME,"news_area")

        for idx, news in enumerate(news_area):
            # 뉴스제목
            title = news.find_element(By.CLASS_NAME,"news_tit")
            # 매체
            press = news.find_element(By.CLASS_NAME,"press")
            # 등록일
            reg_date = news.find_element(By.CSS_SELECTOR,"div.news_info > div.info_group > span")
            # 원문주소
            href = title.get_attribute("href")

            # print(" {}, {}, {}, {}, {}".format(idx, title.text, press.text, reg_date.text, href))

            result += "<div><p><a href='" + href + "'>" + title.text + "</a> "
            result += press.text+" "+reg_date.text + "</p></div>"

print(result)

# 다음에서 이메일 보내기
# 두번째 탭으로 이동
browser.switch_to.window(tabs[1])

# 다음 로그인
# 카카오계정으로 로그인 클릭
browser.find_element(By.CLASS_NAME, "link_kakaoid").click()
time.sleep(1)

# 아이디 입력
id = browser.find_element(By.ID,"id_email_2")
id.clear()
id.send_keys("ford1022@naver.com")

time.sleep(2)

# 비밀번호 입력 
pwd = browser.find_element(By.ID,"id_password_3")
pwd.clear()
pwd.send_keys("young1022")

time.sleep(2)

# 로봇이 아닙니다 클릭


# 로그인 클릭
browser.find_element(By.CLASS_NAME,"btn_confirm").click()
time.sleep(2)

# 메일 클릭
browser.find_element(By.XPATH,'//*[@id="mArticle"]/div[1]/div[2]/ul/li[1]/a').click()

time.sleep(5)

# result 내용 copy
pyperclip.copy(result)

# 메일쓰기 클릭
browser.find_element(By.CLASS_NAME,"btn_write").click()
time.sleep(1)

# 받는 사람 입력
toEmail = browser.find_element(By.ID,"toTextarea")
toEmail.send_keys("받는 사람 이메일")
time.sleep(1)
toEmail.send_keys(Keys.ENTER)

# 제목 입력
mailSubject = browser.find_element(By.ID, "mailSubject")
mailSubject.send_keys("RPA 파이썬 뉴스")
time.sleep(2)
mailSubject.send_keys(Keys.ENTER)

# 하단의 HTML 탭 클릭
browser.find_element(By.CLASS_NAME, "btn_html").click()
time.sleep(3)

# 텍스트 박스 선택 후 복사해 놓은 뉴스 붙여넣기
browser.find_element(By.CSS_SELECTOR,"tx-canvas textarea").send_keys(Keys.CONTROL,"v")
time.sleep(2)

# 보내기 클릭
browser.find_element(By.CLASS_NAME, "btn_toolbar.btn_write").click()

time.sleep(3)
browser.quit()
