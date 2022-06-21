import requests
from bs4 import BeautifulSoup

res = requests.get('https://pythonscraping.com/pages/page3.html')
soup = BeautifulSoup(res.text, "lxml")

# h1 태그 가져오기
h1 = soup.find("h1")
# print(h1)
# print(h1.get_text())

# 상단 내용 가져오기
content = soup.select_one("#content")
# print(content)
# print(content.get_text())

# 모든 img 태그 가져오기
img_list = soup.find_all("img") # soup.select("img")
# print(img_list)

# 타이틀 행 가져오기
row = soup.select("table#giftList > tr:nth-child(1)")
# print(row)
# for item in row:
#     print(item.get_text())

# 테이블 내용 가져오기
table = soup.find("table",id="giftList")
# print(table)
# print(table.get_text())

# 가격만 가져오기
cost_list = soup.select("tr.gift")
for tr in cost_list:
    # print(cost)
    print(tr.find_all("td")[2].get_text())

