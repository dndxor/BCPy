import turtle
import random

## 함수 선언 부분 ##
def  screenLeftClick(x, y):
    turtle.pendown()
    turtle.goto(x, y)

def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)

def  screenMidClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.fillcolor((r, g, b))

## 변수 선언 부분 ##
pSize = 3
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()
