import turtle as t

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

def newx(x):
    global step
    return x / step

def newy(y):
    global step
    return y / step

##[함수] x, y축 좌표 그리기
def draw_xy(wsize, step, hide=0) :
    if hide :
        t.hideturtle()
    line(-wsize, 0, wsize, 0)      # x축 라인
    line(0, -wsize, 0, wsize)      # y축 라인

    for i in range(-wsize, wsize, step) :
        line(i, -5, i, 5)      # x축 눈금
        txtwrite(i-5, -20, newx(i))
    for i in range(-wsize, wsize, step) :
        line(-5, i, 5, i)      # y축 눈금
        if i != 0:
            txtwrite(10, i-5, newy(i))

def draw_fn(wsize, step, direc, a, b, c) :
    for i in range(0, wsize, direc) :
        x1 = newx(i)    #i / step
        y1 = a * (x1 * x1) + b * (x1) + c
        x2 = x1 + newx(1)   #(1/step)
        y2 = a * (x2 * x2) + b * (x2) + c
        if (abs(x1*step) > abs(wsize)) or (abs(y1*step) > abs(wsize)) :
            break      #window 초과 시 나가기
        line(x1*step, y1*step, x2*step, y2*step)

## x, y축 좌표 그리기
t.speed(0)
wsize = 500    #+축 크기 pixel
step = 50      #눈금 간격 pixel(1로 표시되는 길이의 pixel값)

## y = a*(x*x) + b*(x) + c
inlist = [int(x) for x in input(">ax**2 + bx + c의 a b c 입력: ").split()]
a = inlist[0]
b = inlist[1]
c = inlist[2]
draw_xy(wsize, step)
draw_fn(wsize, step, 2, a, b, c)       #(+)축 그리기
draw_fn(-wsize, step, -2, a, b, c)     #(-)축 그리기

t.exitonclick()  # 실행 창을 닫지 않도록