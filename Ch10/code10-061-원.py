from turtle import *
color("black", "gray")

def draw_circle(x, y, r = 100) :
    goto(x, y)
    begin_fill()
    circle(r)
    end_fill()
    return (3.14 * r ** 2)

write("원의 면적 = %d" % draw_circle(0, 0))
stamp()
write("원의 면적 = %d" % draw_circle(300, 0, 50))
stamp()

exitonclick()

