from shutil import ExecError
from urllib import request
from urllib.request import urlopen,Request
from fake_useragent import UserAgent


url="https://isplus.joins.com/2022/06/09/sports/football/20220609151300093.html"
try:

    userAgent = UserAgent()
    headers ={"user-agent":userAgent.chrome}

    request_url = Request(url)
    res = urlopen(request_url).read().decode("utf-8")
    # print(res)
    print(request_url.header_items()) 
    # [('Host', 'isplus.joins.com'), ('User-agent', 'Python-urllib/3.10')]
except Exception as e:
    print(e)