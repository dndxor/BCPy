# 오늘의 뉴스 검색하기

from urllib import request
from bs4 import BeautifulSoup

target = request.urlopen("https://news.daum.net/ranking/popular")
soup = BeautifulSoup(target, "html.parser")

print("*** {0} ***\n".format(soup.title.string))
news = soup.select('div > strong > a')

rank = 1
for title in news :
    print("[{0:2d}] {1}".format(rank, title.get_text())) # title.text와 동일
    rank += 1
