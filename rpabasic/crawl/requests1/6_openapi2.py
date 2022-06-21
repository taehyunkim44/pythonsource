# 도서검색
# 도서명, link, 출판사, 출판일
import requests
from openpyxl import Workbook
from datetime import datetime

client_id = "_lfO7lk3pV4tTMFHiBzb"
client_secret = "_ERfhzVqcL"

url = "https://openapi.naver.com/v1/search/book.json"

headers = {"X-Naver-Client-Id": client_id,"X-Naver-Client-Secret": client_secret}

start, num = 1,0
for idx in range(1):
    start_num = start + (idx * 100)

    url = (
        "https://openapi.naver.com/v1/search/book.json?query=마이클 샌델&display=100&start=1"
        + str(start_num)
    )
    # print(url)

    res = requests.get(url,headers=headers)

    data = res.json()

    for item in data['items']:
        num += 1
        print(num, item["title"],item["link"],item["publisher"],item["pubdate"])
