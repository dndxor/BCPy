#벌집 그리기
from turtle import *

setup(1000, 1000)

for _ in range(6): # 6개의 정육각형을 위한 반복
    for _ in range(6): # 하나의 모양을 이루는 6개의 변을 위한 반복
        fd(80)
        lt(60)
    fd(80); rt(60) # 다음 모양을 그리기 위한 이동과 회전

exitonclick()  # 실행 창을 닫지 않도록