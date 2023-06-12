from bs4 import BeautifulSoup

f = open("example.html", "r", encoding="utf-8")
html = f.read()
soup = BeautifulSoup(html, "html.parser")

#print(soup.prettify())
#print(soup.get_text())
#print(soup.title)
#print(soup.title.string) 
#print(soup.find('a'))
#print(soup.find('a').string)
#print(soup.find_all('a'))

#print(soup.find('a', {'id':'album'})) # 태그명, {속성:속성값}
#print(soup.find(id='album')) # id=id 속성값

#print(soup.find('p', {'class':'song'})) # 태그명, {속성:속성값}
#print(soup.find('p', 'song'))  # 태그명, class 속성값

#print(soup.select_one('i').string)
#print(soup.select('i'))
#print(soup.select_one('p.song'))
#print(soup.select_one('p.song').string)

print(soup.select_one('p > i').string)

