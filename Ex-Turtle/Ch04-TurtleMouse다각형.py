import turtle
import random

## 함수 선언 부분 ##
def render(n, outAngle, step):
    turtle.pendown()
    for i in range(n):
        turtle.forward(step)
        turtle.left(outAngle)

def  screenLeftClick(x, y):
    turtle.pendown()
    turtle.goto(x, y)

def  screenRightClick(x, y):
    turtle.penup()
    turtle.goto(x, y)
##    turtle.write("    (%d,%d)" % (x, y))

def  screenMidClick(x, y):
    global r, g, b
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))
    turtle.fillcolor((r, g, b))
    turtle.penup()
    turtle.goto(x, y)

    ''' 다각형 그리기(호출)'''
    n = random.randrange(3, 8)      #다각형 모양
    intAngle = 180 * (n - 2) / n    #한 내각의 크기
    outAngle = 180 - intAngle       #한 외각의 크기

    step = random.randrange(10, 150)    #다각형 한변 길이
    render(n, outAngle, step)           #다각형 그리기 함수 호출

## 변수 선언 부분 ##
pSize = 3
r, g, b = 0.0, 0.0, 0.0

## 메인 코드 부분 ##
turtle.title('거북이로 그림 그리기')
turtle.shape('turtle')
##turtle.setup(width=1000, height=800)
turtle.pensize(pSize)

turtle.onscreenclick(screenLeftClick, 1)
turtle.onscreenclick(screenMidClick, 2)
turtle.onscreenclick(screenRightClick, 3)

turtle.done()   ## Event Loop 이벤트를 계속 받아 처리
