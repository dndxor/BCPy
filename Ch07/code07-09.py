#스크린 세이버 만들기
from turtle import *
from random import *

x, y, radius = 0, 0, 0
colorList=['red', 'yellow', 'green', 'orange', 'blue', 'violet',
           'tan', 'brown', 'navy', 'cyan']

setup(1200, 800)    # 창 크기
bgcolor("black")    # 배경 색상
speed(0)            # 그리기 최고 속도

for i in range(30):
    x = randint(-500, 500)
    y = randint(-400, 300)
    radius = randint(80, 130)
    penup()
    goto(x, y)
    pendown()
    color(choice(colorList))     # 리스트의 색상 하나를 선택해서 채우기 색으로 설정
    begin_fill()
    circle(radius)
    end_fill()
