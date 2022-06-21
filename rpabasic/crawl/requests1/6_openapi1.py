# naver open api 이용하기
import requests
from openpyxl import Workbook
from datetime import datetime
import re

# 엑셀
wb = Workbook()
ws = wb.active
ws.title = "키보드1000"

ws.column_dimensions["B"].width = 60
ws.column_dimensions["C"].width = 80
ws.column_dimensions["D"].width = 15
ws.append(["순위","상품명","상세주소url","최저가"])

client_id = "_lfO7lk3pV4tTMFHiBzb"
client_secret = "_ERfhzVqcL"

url = "https://openapi.naver.com/v1/search/shop.json"

headers = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret": client_secret}

# 주소 생성
# url = "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start=1"
# url = "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start=101"
# url = "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start=201"
# url = "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start=301"

start,num = 1, 0
for idx in range(10):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/shop.json?query=키보드&display=100&start="
        +str(start_num)
    )
    print(url)

    res = requests.get(url,headers=headers)

    # json 데이터 확인
    # print(res.json())
    data = res.json()
    for item in data['items']:
        num += 1

        # 제품명에 태그 들어간 부분 제거하고 저장
        # <>내용</> <b>아이폰</b> <h1>아이폰</h1>
        title = re.sub("<.+?>","",item["title"])
        print(title, item["link"],item["lprice"])
        ws.append([num, title, item["link"], item["lprice"]])

    # 파일명 gmaket_오늘날짜.xlsx
    today = datetime.now().strftime("%y%m%d")
    filename = f"navershop_{today}.xlsx"
    # 엑셀 저장
    wb.save("./rpabasic/crawl/download/" + filename)