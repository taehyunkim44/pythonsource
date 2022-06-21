from re import A
import requests
from bs4 import BeautifulSoup

url = "https://www.gmarket.co.kr"

res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")
# print(soup.prettify())

# 1차 카테고리 추출하기
# one_depth = soup.find_all("a",class_="link__1depth-item",limit=9)
# print(one_depth)
# for item in one_depth:
#     print(item.get_text())


# 2차 카테고리 추출하기
# two_depth = soup.find_all("div",class_="box__2depth-list")
# for item2 in two_depth:
#     print(item2.get_text())

# item__2depth = soup.find_all("li","list-item__2depth",limit=69)
item__2depth = soup.find_all("li","list-item__2depth")
print(len(item__2depth))
for item in item__2depth:
    # print(item)
    print(item.string) # get_text() : 태그(자식태그 포함)가 가지고 있는 모든 문자열 가져오기
                       # string :  태그가 가지고 있는 문자열만 가져오기
                       
# for depth in item__2depth:
#     href = depth.find("a")['href']
#     print(depth.get_text(),href)