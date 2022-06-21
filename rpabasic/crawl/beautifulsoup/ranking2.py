# https://news.nate.com/rank/interest?sc=ent 랭킹 뉴스 추출 + 엑셀저장(nate_오늘날짜.xlsx)
# 시트명 : 연예랭킹뉴스
# 제목, 기사제공자(연합뉴스..)

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook
from datetime import datetime # 오늘 날짜
import re

# 엑셀
wb = Workbook()
ws = wb.active
ws.title = "연예랭킹뉴스"
ws.column_dimensions['A'].width = 70
ws.column_dimensions['B'].width = 15
# 제목 행 추가
ws.append(["기사제목", "신문사"])


url = "https://news.nate.com/rank/interest?sc=ent"

res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")

# 1~5위 가져오기(타이틀, 기사작성자)
# div.mduSubjectList f_clear
top5_list = soup.select("div.mduSubjectList")
# print(top5_list)

# 6~50위 가져오기
top45_list = soup.select("#postRankSubject li")

for idx, news in enumerate(top5_list,1):
    # 타이틀
    title = news.select_one("a strong").get_text()
    # 신문사 
    media_date = news.select_one("span.medium").get_text()

    # re.sub()
    pattern = re.compile("[\d-]+")
    media = re.sub(pattern,"",media_date)
    print(f"{idx} : {title} - {media}")


    # split() ==> list ['마이데일리','2022-06-21']
    # media = pattern.split(media_date)
    # print(f"{idx} : {title} - {media[0]}")

    ws.append([title, media])


for idx, news in enumerate(top45_list,6):
    # 타이틀    
    title = news.select_one("a").get_text()
    # 신문사 
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
    ws.append([title, media])


# 파일명 nate_오늘날짜.xlsx
today = datetime.now().strftime("%y%m%d")
filename = f"nate_{today}.xlsx"
# 엑셀 저장
wb.save("./rpabasic/crawl/download/"+filename)