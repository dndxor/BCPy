# 공의 포물선 그리기

from turtle import *
from random import *

frame = randrange(1, 30)

def draw_arc(x) :       # 함수 정의
    y = 40 * x - 2 * (x ** 2)
    if y >= 0 :
        goto(x * frame, y)
        write("(%d,%d)" %(x, y))
        stamp()
    return y

shape('classic')          # 터틀 모양 설정
sec = 1                   # 시간(초)의 초기화
while draw_arc(sec) > 0 : # 공이 지면 위에 있는 동안 반복
        sec += 1          # 1초 증가

penup()
goto(0, -40)
pendown()
write("공이 떨어지는 데 %d초 걸렸네요." % sec)

exitonclick()
