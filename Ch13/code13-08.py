# cgv 무비차트

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("http://www.cgv.co.kr/movies/")
soup = BeautifulSoup(target, "html.parser")

print('*** 무비차트 ***\n') #웹사이트 구조 변경으로 인한 코드 수정

movies = soup.select('strong.title')
rates = soup.select('strong.percent > span')

num = 1
for m in zip(movies, rates):
    title = m[0].text
    rate = m[1].text
    print("[{0}] {1} (예매율 {2})".format(num, title, rate))
    num = num + 1
