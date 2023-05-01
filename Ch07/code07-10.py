# 버킷 리스트 관리하기

menu = 0
bucket = []

while True :
    menu = int(input("메뉴 선택(1.추가 2.삭제 0.종료) : "))
    if type(menu) is not int:
        continue
    if menu == 1 :
        bucket.append(input("추가할 내용 : "))
    elif menu == 2 :
        bucket.remove(input("삭제할 내용 : "))
    elif menu == 0 :
        print("프로그램을 종료합니다.")
        break
    else :
        print("메뉴 선택 오류입니다. 다시 선택하세요.")
        continue

    print('*' * 30)
    for x in bucket :
            print(x)
    print('*' * 30)
