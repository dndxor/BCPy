import turtle

turtle.shape('turtle')
turtle.goto(0, 0)

n = int(input("변의 수 입력(3~8) : "))
step = int(input("한변 길이(10~150) : "))
intAngle = 180 * (n - 2) / n
outAngle = 180 - intAngle

for i in range(n):
    turtle.forward(step)
    turtle.left(outAngle)

turtle.exitonclick()  # 실행 창을 닫지 않도록 추가한 문장
