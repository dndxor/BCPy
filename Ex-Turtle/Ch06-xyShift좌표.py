import turtle as t
win = t.Screen()    #Window screen 객체 생성
w_wsize = 1600    #window 가로 크기 pixel
w_hsize = 900     #window 세로 크기 pixel
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
def newx(x=0) :
    global l_shift
    return (x - l_shift)

##Shift된 new y-좌표 구하기
def newy(y=0):
    global d_shift
    return (y - d_shift)

##[함수] x, y축 좌표 그리기
def draw_xy(wsize, hsize, step) :
    line(-wsize, newy(0), wsize, newy(0))      # x축 라인
    line(newx(0), -hsize, newx(0), hsize)      # y축 라인

    for i in range(0, -wsize, -step) :
        line(i, newy(-5), i, newy(5))      # x(-)축 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))
    for i in range(step, wsize, step) :
        line(i, newy(-5), i, newy(5))      # x(+)축 눈금
        txtwrite(i-10, newy(0)-20, i-newx(0))

    for i in range(0, -hsize, -step) :
        line(newx(-5), i, newx(5), i)      # y(-)축 눈금
        txtwrite(newx(0)+10, i-10, i-newy(0))
    for i in range(step, hsize, step) :
        line(newx(-5), i, newx(5), i)      # y(+)축 눈금
        txtwrite(newx(0)+10, i-10, i-newy(0))

##.........메인 시작.........##
##변수 초기화
l_shift = 400     #x축 left로 shift pixel 값
d_shift = 100     #y축 down으로 shift pixel 값
wsize = int(w_wsize / 2)    #x(+)축 길이
hsize = int(w_hsize / 2)    #y(+)축 길이
step = 100      #눈금 간격 pixel

## x, y축 좌표 그리기
t.hideturtle()
t.speed(0)

draw_xy(wsize, hsize, step)

t.exitonclick()  # 실행 창을 닫지 않도록
##.........메인 끝.........##