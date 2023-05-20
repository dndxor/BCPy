import time
# 공의 포물선 그리기
from turtle import *

def draw_arc(x, theta=45) :       # 함수 정의
    y = 40 * x - 2 * (x ** 2)
    if y >= 0 :
        goto(x*(90-theta), y)
        write("(%d,%d)" %(x, y))
        stamp()
    return y

shape('classic')          # 터틀 모양 설정
for th in range(90, 0-1, -10):
    sec = 1                   # 시간(초)의 초기화
    goto(0, 0)
    pendown()
    while draw_arc(sec, th) > 0 : # 공이 지면 위에 있는 동안 반복
        time.sleep(0.1)
        sec += 1          # 1초 증가
    penup()

penup()
goto(0, -40)
pendown()
write("공이 떨어지는 데 %d초 걸렸네요." % sec)

exitonclick()
