import requests
from bs4 import BeautifulSoup
from urllib.request import urlretrieve

res = requests.get("https://ko.wikipedia.org/wiki/%EC%84%9C%EC%9A%B8_%EC%A7%80%ED%95%98%EC%B2%A0")

soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())

# 사진 저장
#  #mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img
image1 = soup.select_one("#mw-content-text > div.mw-parser-output > table.infobox > tbody > tr:nth-child(1) > td > a > img")
print(image1)
print(image1["src"]) # http:/upload.wikimedia.org/~~

# 이미지 다운로드 - urlretrieve

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"
# urlretrieve("이미지 원본 경로","다운로드 받을 경로")
# urlretrieve("http:"+image1["src"],path + "subway1.jpg")

print()
# 두 번째 사진 저장
image2 = soup.select_one("#mw-content-text > div.mw-parser-output > div.thumb.tright > div > a > img")
print(image2["src"])
urlretrieve("http:"+image2["src"],path + "anniversiry.jpg")
