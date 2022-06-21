# 저장하고 싶은 이미지

import urllib.request as req

img_url="https://rank5.kr/news/photo/202108/8035_25110_2712.jpg"
file_url="https://liquipedia.net/"

path="./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path+"strong.png")
    file2, header2 = req.urlretrieve(file_url, path+"liquipedia.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)