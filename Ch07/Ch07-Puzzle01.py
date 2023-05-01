##모듈 임포트
import random

##전역약변수 정의
row, col = (0, 0)
puzzle = []

##함수 정의
def rand_puzzle() :
    global puzzle, row, col
    arr = [i for i in range(row*col)]
    arr = random.sample(arr, row*col)
    for i in range(0, len(arr), col):
        puzzle.append(arr[i:i + col])

def prt_puzzle() :
    global puzzle, row, col
    print("\n")
    for i in range(row) :
        for j in range(col) :
            if puzzle[i][j] == 0 :
                print("%4s" %"    ", end = "")
            else :
                print("%4s" %str(puzzle[i][j]), end = "")
        print("\n")

##====== 메인 시작 ======##
## 변수 초기화
col = int(input("열 개수는? "))
row = col

rand_puzzle()
prt_puzzle()
##====== 메인 끝 ======##
