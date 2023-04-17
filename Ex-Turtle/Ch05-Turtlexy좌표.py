import turtle as t

t.speed(3)
##t.hideturtle()

##[함수] (x1, y1) - (x2, y2) 직선 그리기
def line(x1, y1, x2, y2):
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y2)

##[함수] (x,y)에 텍스트 쓰기
def txtwrite(x, y, text):
    t.up()
    t.goto(x, y)
    t.down()
    t.write(text)

##[함수] x, y축 좌표 그리기
def draw_xy(wsize, step, hide=0) :
    if hide :
        t.hideturtle()
    line(-wsize, 0, wsize, 0)      # x축 라인
    line(0, -wsize, 0, wsize)      # y축 라인

    for i in range(-wsize, wsize, step) :
        line(i, -5, i, 5)      # x축 눈금
        if i != 0:
            txtwrite(i-10, -20, i)
    for i in range(-wsize, wsize, step) :
        line(-5, i, 5, i)      # y축 눈금
        if i != 0:
            txtwrite(10, i-5, i)

wsize = 500
step = 100
draw_xy(wsize, step)

'''
## x, y축 좌표 그리기
line(-500, 0, 500, 0)      # x축 라인
line(0, -500, 0, 500)      # y축 라인

for i in range(-500, 500, 100) :
    line(i, -5, i, 5)      # x축 눈금
    if i != 0:
        txtwrite(i-10, -20, i)
for i in range(-500, 500, 100) :
    line(-5, i, 5, i)      # y축 눈금
    if i != 0:
        txtwrite(20, i-10, i)
'''
t.exitonclick()  # 실행 창을 닫지 않도록