# 다나와 로그인

import requests
from bs4 import BeautifulSoup

# payload
login_info={
    "redirectUrl": "https://www.danawa.com",
    "loginMemberType": "general",
    "id": "eiiyy12",
    "isSaveId": "true",     
    "password": "young1022!",
}

# 헤더 정보
headers ={
    "Referer":"https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2F",
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
}

# 세션을 이용
with requests.Session() as s:

    # 로그인
    res = s.post("https://auth.danawa.com/login",login_info,headers=headers)
    # print(res.text)

    # 주문/배송 조회
    res = s.get("https://buyer.danawa.com/order/Order/orderList",headers=headers)
    
    # 현재 페이지 파싱
    soup = BeautifulSoup(res.text, "lxml")

    # 아이디 찾기
    user_id = soup.find("p",class_="user")    
    print(user_id)
    # print(user_id.get_text())

    if user_id is None:
        # 강제 예외 발생
        raise Exception("Login 실패, 아이디나 비밀번호 확인")
    
# 상단 메뉴 가져오기
# menu = soup.find("ul",class_="info_list")
# print(menu)
# copy - selector (css selector)
# select(): element를 리스트로 가져옴

menu_list = soup.select("div > ul.info_list > li")
print(menu_list)

for menu in menu_list:
    # 메뉴명, 수량
    proc, val = (
        menu.find("span").get_text().strip(),
         menu.find("strong").get_text().strip()
    )
    print(f"{proc}:{val}")