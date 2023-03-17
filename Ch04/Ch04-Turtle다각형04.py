import turtle
import random

## 함수 선언 부분 ##
def render(n, outAngle, step):
    for i in range(n):
        turtle.forward(step)
        turtle.left(outAngle)

## 변수 선언 부분 ##
n = random.randrange(3, 8)          ##변의 수
step = random.randrange(10, 150)    ##한변 길이
intAngle = 180 * (n - 2) / n
outAngle = 180 - intAngle

## 메인 코드 부분 ##
turtle.title('거북이로 정다각형 그리기')
turtle.shape('turtle')
turtle.goto(0, 0)

render(n, outAngle, step)

turtle.exitonclick()  # 실행 창을 닫지 않도록
