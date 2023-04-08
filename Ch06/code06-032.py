import random                   # random 모듈 불러오기
number = 0 # 입력하는 값을 저장할 변수

while True :
    answer = random.randint(1, 20)  # 1에서 20 사이의 랜덤 정수 저장
    cnt = 0
    while number != answer:
        number = int(input("숫자 입력(1~20) : "))
        cnt += 1
        print("[%02d]" % cnt, end=' ')
        if number > answer:         # 입력한 값이 정답보다 큰 경우
            print("↓")
        elif number < answer:       # 입력한 값이 정답보다 작은 경우
            print("↑")
        else:
            print("★정답★")

    if cnt <= 5 :
        print("당신이 이겼습니다.")
    else :
        print("당신이 졌습니다.")

    yn = input(">다시 할까요(y/n)? ")
    if yn == 'y' or yn == 'Y' : 
        continue 
    else :
        break 
