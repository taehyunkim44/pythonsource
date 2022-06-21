import urllib.request as req

# 이미지, html 파일 다운로드 

img_url = "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMjA1MjRfMTUx%2FMDAxNjUzMzU5NjM4MDUz.N89_OgZEb3KT1KyOzCut3h0axotp4oD1nm1yYQkVUu4g.GYlEDmBCT-xLrh9-h7PPm8Yw0ZA0bmvV0lVWPCy4qRog.JPEG%2FIRPyp4EftpquF_53lIm7_cSi7asw.jpg&type=sc960_832"
file_url = "https://www.naver.com"

# 다운로드 받을 경로
path = "./rpabasic/crawl/download/"

try:
    file1, header1 = req.urlretrieve(img_url, path+"dog.png")
    file2, header2 = req.urlretrieve(file_url, path+"naver.html")
except Exception as e:
    print(e)
else:
    print(header1)
    print()
    print(header2)
