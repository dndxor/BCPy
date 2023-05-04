#도서 가격 검색하기

books = {'여행의 이유':13500, '소년이로':13000, '희랍인 조르바':9000,
         '세 여자':14000, '아픔이 길이 되려면':18000}
print("검색 가능 도서 :", list(books.keys())) # 도서명을 모두 출력
print('-'*35)

while True:
    bookName = input("도서명 입력(검색 종료는 0) : ")
    if bookName in books:
        print(bookName, "=", books.get(bookName), "원\n")
    elif bookName == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("검색 가능한 도서가 아닙니다.\n")
