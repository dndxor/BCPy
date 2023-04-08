# 정다각형 그리기

from turtle import *

setup(500, 500)
pensize(10)     # 펜 두께 설정
pencolor('red') # 펜 색상 설정 

while True :    # 무한 반
    shape = int(input("다각형 모양(3~6, 종료는 0) : "))
    if shape == 0 : break   # 종료 조건
    if shape < 3 or shape > 6 :     # 입력 오류
        print("모양을 다시 입력하세요.")
        continue
       
    clear()     # 이전 그림을 지우기
    for _ in range(shape) :
        fd(100)
        lt(360 / shape)   # 회전 각도(=외각의 크기)는 360/꼭지점의 수
    
print("그리기를 종료합니다.")
bye() # 터틀 그래픽스 종료
