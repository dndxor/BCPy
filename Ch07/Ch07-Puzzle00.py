##모듈 임포트
import random

##전역약변수 정의
row, col = (4, 4)
puzzle = []

arr = [i for i in range(row*col)]
arr = random.sample(arr, row*col)

for i in range(0, len(arr), col):
    puzzle.append(arr[i:i+col])
print(puzzle)

##====== 메인 시작 ======##
## 변수 초기화

##====== 메인 끝 ======##
