import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

url = "https://n.news.naver.com/mnews/article/016/0002001716?sid=100"
headers = {"user-agent":UserAgent().chrome}

res = requests.get(url, headers=headers)

soup = BeautifulSoup(res.text,"lxml")

# 특정 엘리먼트 찾기 - 1. 태그 이용(가장 처음에 만나는 태그만 가져오기)
print(soup.h2)

# 특정 엘리먼트 찾기 - 2. find(), find_all(), find_*()
h2_ele = soup.find("h2",class_="media_end_head_headline")
print(h2_ele)