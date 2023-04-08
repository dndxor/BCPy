import turtle
import random

def render(n, outAngle, step):
    for i in range(n):
        turtle.forward(step)
        turtle.left(outAngle)

turtle.shape('turtle')
turtle.goto(0, 0)

n = random.randrange(3, 8)          ##변의 수
intAngle = 180 * (n - 2) / n
outAngle = 180 - intAngle
step = random.randrange(10, 150)    ##한변 길이

render(n, outAngle, step)

turtle.exitonclick()  # 실행 창을 닫지 않도록
