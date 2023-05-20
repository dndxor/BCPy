#터틀 그림판

from turtle import *

def go(x,y):    # 마우스 클릭 때의 동작을 정의, 현재 좌표를 인수로 사용
    goto(x,y)

def east() :    # 오른쪽 방향 키가 눌렸을 때의 동작
    setheading(0) #이동 방향 설정
    forward(10)

def north() :   # 위쪽 방향 키가 눌렸을 때의 동작
    setheading(90) 
    forward(10)

def west() :    # 왼쪽 방향 키가 눌렸을 때의 동작
    seth(180)
    forward(10)

def south() :   # 아래쪽 방향 키가 눌렸을 때의 동작
    seth(270)
    forward(10)

hideturtle() # 터틀을 화면에서 숨김
pensize(10)
pencolor("blue")

onscreenclick(go)   # 마우스를 클릭하면 go() 함수를 실행
onkeypress(north, "Up") # 키 이벤트 처리
onkeypress(south, "Down")
onkeypress(west, "Left")
onkeypress(east, "Right")

listen() #키 입력 대기

