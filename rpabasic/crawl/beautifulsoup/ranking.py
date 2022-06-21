# https://news.nate.com/rank/interest?sc=ent 랭킹 뉴스 추출
# 제목, 기사제공자(연합뉴스..)

import requests
from bs4 import BeautifulSoup

# res = requests.get("https://news.nate.com/rank/interest?sc=ent")
# soup = BeautifulSoup(res.text,"lxml")

# title_list = soup.select("div > a > span.tb > strong")
# print(title_list)

# offer_list = soup.select("div > span.medium")
# print(offer_list)

# for title in title_list:
#     print(title.get_text().strip())
# print("*" * 80)

# for offer in offer_list:
#     print(offer.get_text().strip())
# print("*" * 80)

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
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")


for idx, news in enumerate(top45_list,6):
    # 타이틀    
    title = news.select_one("a").get_text()
    # 신문사 
    media = news.select_one("span.medium").get_text()
    print(f"{idx} : {title} - {media}")
