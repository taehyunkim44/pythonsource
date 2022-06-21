import urllib.request as req

targer_url = [
    "https://search.pstatic.net/common/?src=http%3A%2F%2Fpost.phinf.naver.net%2FMjAyMjA1MjRfMTUx%2FMDAxNjUzMzU5NjM4MDUz.N89_OgZEb3KT1KyOzCut3h0axotp4oD1nm1yYQkVUu4g.GYlEDmBCT-xLrh9-h7PPm8Yw0ZA0bmvV0lVWPCy4qRog.JPEG%2FIRPyp4EftpquF_53lIm7_cSi7asw.jpg&type=sc960_832",
    "https://www.naver.com",
]

# 다운로드 받을 경로
path_list = [
    "./rpabasic/crawl/download/dog.png",
    "./rpabasic/crawl/download/naver.html",
]

for i, url in enumerate(targer_url):

    try:
        res = req.urlopen(url)
        
        contents = res.read()

        print("--------------------")
        print("Header info-{} : {}".format(i,res.info()))
        print("http status : {}".format(res.getcode()))
        print("--------------------")

        with open(path_list[i],"wb") as c:
            c.write(contents)
    except Exception as e:
        print(e)
    else:
        print("성공")