import turtle

turtle.shape('turtle')
turtle.goto(0, 0)

n = 4
step = 100
intAngle = 180 * (n - 2) / n
outAngle = 180 - intAngle

turtle.forward(step)
turtle.left(outAngle)
turtle.forward(step)
turtle.left(outAngle)
turtle.forward(step)
turtle.left(outAngle)
turtle.forward(step)
turtle.left(outAngle)

turtle.exitonclick()           #실행 창을 닫지 않도록 추가한 문장