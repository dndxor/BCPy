# 도서 목록 관리하기

book = ''      # 입력하는 도서명을 저장하는 변수
bookList = []  # 도서 목록을 저장하는 리스트
number = 0     # 출력할 때 표시할 순서 번호

print("입력을 종료하려면 [Enter] 키를 누르세요.")
print('=' * 30)

while True :
    book = input("도서명 입력 : ")
    if book == '' :     # 도서명을 입력하지 않고 엔터를 누르면, 빈문자열이 된다.
        break
    bookList.append(book)
        
bookList.sort()  # 리스트의 정렬

print('=' * 30)  # 결과 출력
for b in bookList :
    number += 1
    print(number, ':', b)
