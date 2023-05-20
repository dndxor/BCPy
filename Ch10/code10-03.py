from turtle import *
color("yellow", "gray")

def draw_circle() :
    begin_fill()
    circle(100)
    end_fill()

for i in range(3) :
    goto(0, i * 20)
    draw_circle()

goto(300, i * 20)
draw_circle()

goto(-300, i * 20)
draw_circle()

exitonclick()
'''
# 함수를 사용하지 않고 반복문으로 실행
for i in range(3) :
    goto(0, i * 20)
    begin_fill()
    circle(100)
    end_fill()

goto(300, i * 20)
begin_fill()
circle(100)
end_fill()

goto(-300, i * 20)
begin_fill()
circle(100)
end_fill()

'''