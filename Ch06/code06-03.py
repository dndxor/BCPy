import random                   # random 모듈 불러오기
answer = random.randint(1, 20)  # 1에서 20 사이의 랜덤 정수 저장 
number = 0                      # 입력하는 값을 저장할 변수

while number != answer:
    number = int(input("숫자 입력(1~20) : "))

    if number > answer:         # 입력한 값이 정답보다 큰 경우
        print("↓")
    elif number < answer:       # 입력한 값이 정답보다 작은 경우
        print("↑")
    else:
        print("★정답★")
