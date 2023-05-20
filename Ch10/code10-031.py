from turtle import *    ##모듈명 생략 가능##

##color("yellow", "gray")   ##color(펜컬러, 필컬러)
pencolor("yellow")
fillcolor("red")
speed(10)

def draw_circle(x=0, y=0, r=100) :
    goto(x, y)
    begin_fill()
    circle(r)
    end_fill()

for i in range(3) :
    r = 100
    draw_circle(0, i * 20, r)
    

'''
# <참고>
'''

goto(300, i * 20)
draw_circle(50)

goto(-300, i * 20)
draw_circle(200)


'''
# 함수를 사용하지 않고 반복문으로 실행
from turtle import *

color("yellow", "gray")
for i in range(3) :
    goto(0, i * 20)
    begin_fill()
    circle(100)
    end_fill()

for i in range(2) :
    goto(300, i * 20)
    begin_fill()
    circle(100)
    end_fill()

goto(-300, i * 20)
begin_fill()
circle(100)
end_fill()
'''
