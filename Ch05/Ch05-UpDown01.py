# random 모듈 불러오기
import random as r
# 1에서 20 사이의 랜덤 정수 저장
rnum = r.randint(1, 20)
print("1~20 중에 하나의 난수를 발생했습니다.")
innum = 0

while innum != rnum:
    innum = int(input("숫자 입력(1~20) : "))
    if innum > rnum:
        print("Down")
    else:
        if innum < rnum:
            print("Up")
        else:
            if innum == rnum:
                print("OK!")