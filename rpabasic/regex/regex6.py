import re
import requests
from bs4 import BeautifulSoup

res = requests.get("https://www.naver.com")
soup = BeautifulSoup(res.text,"lxml")

# h 태그로 시작하는 모든 태그 찾기
# h1 ~ h6
print(soup.find_all(re.compile("h\d")))

# 이미지 파일을 가져오기 - 1.jpg, ex.jpg    
print(soup.find_all("img",attrs={"src":re.compile(".+\.jpg")}))
print(soup.find_all("img",attrs={"src":re.compile(".+\.jpg|png")}))