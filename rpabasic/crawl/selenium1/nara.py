# 나라장터 용역 공고 자동화
from openpyxl import Workbook
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from bs4 import BeautifulSoup

from  openpyxl import Workbook

# 업무,공고번호,분류,공고명,공고기관,수요기관,계약방법,입력일시,마감일시,원문 상세주소
wb = Workbook()
ws = wb.active
ws.title = '용역공고'
# 제목행 추가
ws.append(["업무","공고번호","분류","공고명","공고기관","수요기관","계약방법","입력일시","마감일시","원문 상세주소"])

# taskClCds=5 용역
# fromBidDt, toBidDt, currentPageNo


browser = webdriver.Chrome()
browser.maximize_window()

for i in range(1, 2):
    url =  "https://www.g2b.go.kr:8101/ep/tbid/tbidList.do?area=&areaNm=&bidNm=&"
    url += "bidSearchType=1&budgetCompare=&detailPrdnm=&detailPrdnmNo=&downBudget=&"
    url += "fromBidDt=2022%2F05%2F24&fromOpenBidDt=&industry=&industryCd=&instNm=&"
    url += "instSearchRangeType=&intbidYn=&orgArea=&procmntReqNo=&radOrgan=1&"
    url += "recordCountPerPage=30&refNo=&regYn=Y&searchDtType=1&searchType=1&"
    url += "strArea=&taskClCds=5&toBidDt=2022%2F06%2F23&toOpenBidDt=&upBudget=&"
    url += "currentPageNo=" + str(i) + "&maxPageViewNoByWshan=2&"

    browser.get(url)

    time.sleep(2)

    # 업무,공고번호,분류,공고명,공고기관,수요기관,계약방법,입력일시(입찰마감일시)
    tbody = browser.find_element(By.XPATH,'//*[@id="resultForm"]/div[2]/table/tbody')
    trs = tbody.find_elements(By.TAG_NAME, "tr")

    for idx, row in enumerate(trs):
        # 업무
        data_1 = row.find_elements(By.TAG_NAME,"td")[0]
        # 공고번호
        data_2 = row.find_elements(By.TAG_NAME,"td")[1]
        # 분류
        data_3 = row.find_elements(By.TAG_NAME,"td")[2]
        # 공고명
        data_4 = row.find_elements(By.TAG_NAME,"td")[3]
        # 공고기관
        data_5 = row.find_elements(By.TAG_NAME,"td")[4]
        # 수요기관
        data_6 = row.find_elements(By.TAG_NAME,"td")[5]
        # 계약방법
        data_7 = row.find_elements(By.TAG_NAME,"td")[6]
        # 입력일시(+마감일시)
        # (2022/06/15 10:00)
        data_8 = row.find_elements(By.TAG_NAME,"td")[7]

        # 입력일시와 마감일시 따로 작업
        reg_date = data_8.text.split("\n")[0]
        end_date = data_8.text.split("\n")[1]

        # 입찰공고 상세 주소
        data_link = row.find_element(By.TAG_NAME,"a").get_attribute("href")

        print(
            data_1.text,
            data_2.text,
            data_3.text,
            data_4.text,
            data_5.text,
            data_6.text,
            data_7.text,
            reg_date,
            end_date,
            data_link,
        )
  
        ws.append(
            [
                data_1.text,
                data_2.text,
                data_3.text,
                data_4.text,
                data_5.text,
                data_6.text,
                data_7.text,
                reg_date,
                end_date,
                data_link,
            ]
        )

        time.sleep(2)

wb.save("./rpabasic/crawl/download/nara.xlsx")

time.sleep(2)
browser.quit()