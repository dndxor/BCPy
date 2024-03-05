## Python 코딩 연습 ##
## 함수 호출 개념 이해
import turtle


def render(n, step=100, rgb=(0, 0, 0)):  # 매개변수 기본값(default value) 지정
    turtle.pencolor(rgb)
    turtle.pendown()

    angle = 360 / n
    for _ in range(n):  # n번 반복
        turtle.forward(step)  # 90pixcel 전진
        turtle.left(angle)  # 좌로 90도 회전


################## 메인 시작 ############
# 4각형 그리기 Raw Coding
n = int(input(">몇 각형(3~n)? "))
step = 100
pencolor = (0, 1, 1)
render(n, rgb=pencolor, step=50)  # 함수 호출: default 매개변수에 대해 원하는 값만 선택 전달(순서 무관)

turtle.exitonclick()  # 실행 창을 닫지 않도록
################# 메인 끝 ##############