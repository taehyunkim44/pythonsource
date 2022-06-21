#네이버 금융 주식 인기 검색 종목

import requests
from bs4 import BeautifulSoup

res = requests.get("https://finance.naver.com/")
# print(res.text)
soup = BeautifulSoup(res.text,"lxml")

# 인기 검색 종목 - 종목명, 현재가격
# stock1 = soup.select("div.aside_area.aside_popular > table > tbody > tr")
# # print(stock1)
# for item in stock1:
#     # 종목명
#     stock_name = item.find('a').get_text()
#     # 현재가격
#     stock_price = item.find("td").get_text()

#     print(stock_name,stock_price)

print()
# 해외 증시
stock2 = soup.select(" div.aside_area.aside_stock > table > tbody > tr")
# print(stock2)
for item in stock2:
    stock_name = item.find('a').get_text()
    stock_price = item.find("td").get_text()

    print(stock_name,stock_price)