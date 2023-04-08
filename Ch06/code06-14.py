#스크린 세이버 만들기
from turtle import *
from random import *

x = 0
y = 0
radius = 0

setup(1200, 800)
bgcolor("black")    # 창 색상 설정
speed(10)           # 그리기 속도 설정
pensize(10)
color("white", "darkgray") # 펜 색상과 채우기 색상 설정

for _ in range(30) : # 30개의 원 그리기
    x = randint(-500, 500)
    y = randint(-400, 300)
    radius = randint(80, 130)
    penup()
    goto(x, y)
    pendown()
    begin_fill()    # 채우기 색상으로 원을 채우기
    circle(radius)
    end_fill()
