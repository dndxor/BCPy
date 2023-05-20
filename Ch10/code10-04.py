from turtle import *
color("yellow", "gray")

def draw_circle(x, y, r) :
    goto(x, y)
    begin_fill()
    circle(r)
    end_fill()

for i in range(3) :
    draw_circle(0, i * 20, 100)

draw_circle(300, 0, 100)
draw_circle(-300, 0, 100)
