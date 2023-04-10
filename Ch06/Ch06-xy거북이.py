import turtle as t
w_wsize = 1000    #window 가로 크기 pixel
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
    line(-wsize, newy(0), wsize, newy(0))           # x축 turtle 라인
    line(-wsize, newy(0)+50, wsize, newy(0)+50)     # x축 rabbit 라인
    line(newx(0), -hsize, newx(0), hsize)           # y축 라인

    for i in range(0, -wsize, -step) :
        line(i, newy(-5), i, newy(5))           #x(-)축 turtle 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))
    for i in range(step, wsize, step) :
        line(i, newy(-5), i, newy(5))           #x(+)축 turtle 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))

    for i in range(0, -wsize, -step) :
        line(i, newy(-5)+50, i, newy(5)+50)      #x(-)축 rabbit 눈금
        txtwrite(i-10, newy(0)-20+50, i-newx(0))
    for i in range(step, wsize, step) :
        line(i, newy(-5)+50, i, newy(5)+50)      #x(+)축 rabbit 눈금
        txtwrite(i-10, newy(0)-20+50, i-newx(0))

##[함수] turtle-rabbit running game
def run_game(ttl, rbt, p_ttl, p_rbt) :
    # turtle 상태 설정
    ttl.speed('fastest')
    ttl.goto(newx(p_ttl), newy(0))
    ttl.showturtle()
    ttl.pendown()
    ttl.speed('slowest')

    # rabbit 상태 설정
    rbt.speed('fastest')
    rbt.goto(newx(p_rbt), newy(50))
    rbt.pendown()
    rbt.showturtle()
    rbt.speed('slowest')

    min = 0
    while p_rbt <= p_ttl :
        min += 1
        p_rbt += 45
        p_ttl += 11

        rbt.pensize(p_rbt%2*3)
        ttl.pensize(p_ttl%2*3)
        rbt.forward(45)
        ttl.forward(11)

        txtwrite(newx(p_rbt), newy(120), '['+str(min)+']')  #rabbit 경과 시간(min)
        txtwrite(newx(p_rbt), newy(100), p_rbt)  #rabbit 위치(m)
        txtwrite(newx(p_ttl), newy(-50-(15*min)), '['+str(min)+'] '+str(p_ttl))  #turtle 위치(m)

##.........메인 시작.........##
##변수 초기화
l_shift = 400   #x축 left로 shift pixel 값
d_shift = 100   #y축 down으로 shift pixel 값
wsize = int(w_wsize / 2)    #x-축 (+)축 길이
hsize = int(w_hsize / 2)    #y-축 (+)축 길이
step = 100      #눈금 간격 pixel

## x, y축 좌표 그리기
t.hideturtle()
t.speed(0)
draw_xy(wsize, hsize, step)

##토끼, 거북이 객체 생성하기
ttl = t.Turtle()    #turtle 객체 생성
ttl.hideturtle()
ttl.penup()
ttl.shape('turtle')
ttl.color('red')

rbt = t.Turtle()    #rabbit 객체 생성
rbt.hideturtle()
rbt.penup()
rbt.shape('triangle')
rbt.color('blue')

##게임 시작
p_ttl = int(t.numinput("위치 값 입력", "거북이 위치(정수: -200~1000)? "))     #turtle 최초 위치
p_rbt = int(t.numinput("위치 값 입력", "토끼 위치(정수: -200~1000)? "))       #rabbit 최초 위치

run_game(ttl, rbt, p_ttl, p_rbt)

t.exitonclick()  # 실행 창을 닫지 않도록
##.........메인 끝.........##