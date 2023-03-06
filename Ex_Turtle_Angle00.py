import turtle as t

def draw_trail(n):
    angle = 360 // n
    for _ in range(n):
        t.forward(100)
        t.left(angle)

################## 메인 시작 ############
t.shape('turtle')

t.goto(0,0)

while True:
    n = int(t.numinput("변의 수 입력: ", "정수로 입력"))

    if n < 3:
        if n == 0:
            break
        else:
            continue
    draw_trail(n)

t.exitonclick()
################# 메인 끝 ##############
