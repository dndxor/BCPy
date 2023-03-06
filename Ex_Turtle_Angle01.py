import turtle as t

def draw_trail(n):
    angle = 360 // n
    for _ in range(n):
        t.forward(100)
        t.left(angle)

################## 메인 시작 ############
t.shape('turtle')

t.goto(0,0)

for i in range(6):
    draw_trail(6)
    t.forward(5)
    t.right(60)

t.exitonclick()
################# 메인 끝 ##############
