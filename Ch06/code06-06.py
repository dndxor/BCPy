menu = 0   # 선택 메뉴
number = 0 # 주문 수량
price = 0  # 상품 단가  
total = 0  # 금액 합계

print("*"*30) # 메뉴 출력
print("[1]팝콘 [2]나쵸 [3]핫도그 [4]음료")
print("주문을 끝내려면 [0]을 입력하세요.")
print("-"*30)

while True:
    menu = int(input("선택 메뉴 : "))
    if menu == 0:
        break
    if menu < 1 or menu > 4:
        print("메뉴 선택 오류...다시 선택하세요.\n")
        continue
    
    if menu == 1: price = 5000		# 조건식과 명령문을 한 줄에 적기 
    elif menu == 2: price = 4000
    elif menu == 3: price = 3500
    else: price = 2000
        
    number = int(input("주문 수량 : "))
    total = total + (number * price)
    print()     # 다른 메뉴를 선택하기 전에 빈 줄 추가
    
print("-"*30)
print("금액 합계는", total, "원입니다.")
