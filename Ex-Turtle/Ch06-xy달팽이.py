import turtle as t
w_wsize = 600    #window 가로 크기 pixel
w_hsize = 600     #window 세로 크기 pixel
win = t.Screen()    #Window screen 객체 생성
win.setup(w_wsize, w_hsize)

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

##Shift된 new x-좌표 구하기
def newx(x) :
    global l_shift
    return (x-l_shift)

##Shift된 new y-좌표 구하기
def newy(y):
    global d_shift
    return (y-d_shift)

##[함수] x, y축 좌표 그리기
def draw_xy(wsize, hsize, step) :
    line(-wsize, newy(0), wsize, newy(0))           # x축 라인
    line(newx(0), -hsize, newx(0), hsize)           # y축 라인

    for i in range(0, -wsize, -step) :
        line(i, newy(-5), i, newy(5))           #x(-)축 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))
    for i in range(step, wsize, step) :
        line(i, newy(-5), i, newy(5))           #x(+)축 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))

    for i in range(0, -hsize, -step) :
        line(newx(-5), i, newx(5), i)      # y(-)축 눈금
        txtwrite(newx(0)+10, i-7, i-newy(0))
    for i in range(step, hsize, step) :
        line(newx(-5), i, newx(5), i)      # y(+)축 눈금
        txtwrite(newx(0)+10, i-7, i-newy(0))

##[함수] running game
def run_game(dal, p_dal) :
    heigh = 0  # 우물 밖 목표 위치(cm)
    days = 0
    p_dal = -p_dal

    dal.speed('fastest')
    dal.goto(newx(0), newy(p_dal))
    dal.left(90)
    dal.showturtle()
    dal.pendown()
    dal.speed('slowest')
    line(newx(-200), newy(p_dal), newx(0), newy(p_dal))           # x축 바닥 라인

    while p_dal < heigh:
        days += 1
        dal.pensize(1)
        if (heigh - p_dal) >= 55 :
            p_dal += 55
            dal.forward(55)
        else :
            dal.forward(abs(heigh - p_dal))
            dal.right(90)
            p_dal = heigh
        txtwrite(newx(50), newy(p_dal), '[' + str(days) + '] ' + str(p_dal))  # 달팽이 현재 위치(m)
        print("%2d일째>%5dcm" % (days, p_dal), end=" ")
        if p_dal >= heigh:
            break
        p_dal -= 13
        dal.pensize(3)
        dal.backward(13)
        print("%5dcm" % (p_dal))

    print("\n>>%d일만에 탈출 성공" % days)

##.........메인 시작.........##

##변수 초기화
l_shift = 0   #x축 left로 shift pixel 값
d_shift = -200     #y축 down으로 shift pixel 값
wsize = int(w_wsize / 2)    #x-축 (+)축 길이
hsize = int(w_hsize / 2)    #y-축 (+)축 길이
step = 100      #눈금 간격 pixel

## x, y축 좌표 그리기
t.hideturtle()
t.speed(0)
draw_xy(wsize, hsize, step)

##토끼, 거북이 객체 생성하기
dal = t.Turtle()    #turtle 객체 생성
dal.hideturtle()
dal.penup()
dal.shape('turtle')
dal.color('red')

##게임 시작
p_dal = int(t.numinput("위치 값 입력", "우물 깊이 값 입력(cm, 양수)? "))    #우물 안 달팽이 위치(cm)

run_game(dal, p_dal)

t.exitonclick()  # 실행 창을 닫지 않도록
##.........메인 끝.........##