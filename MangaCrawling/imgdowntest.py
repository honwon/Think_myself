from urllib import request
import time

url = "https://newtoki3.org/data/file/comic/15756916271225.jpg"

# time check
start = time.time()

# request.urlopen()
res = request.urlopen(url).read()

# 이미지 다운로드 시간 체크
print(time.time() - start)


