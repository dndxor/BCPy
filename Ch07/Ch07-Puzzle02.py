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

def find_zero():
    for i in range(row) :
        for j in range(col) :
            if puzzle[i][j] == 0 :
                return row*i+j

##====== 메인 시작 ======##
## 변수 초기화
col = int(input("열 개수는? "))
row = col

rand_puzzle()
prt_puzzle()

zero_seq = find_zero()
r = zero_seq // row  # zero 위치 행
c = zero_seq % row  # zero 위치 열
print("r: %d, c: %d" %(r, c))

'''
for i in range(row):
    for j in range(col):
        if puzzle[i][j] == 0:
            print("row: %d, col: %d" %(i, j))
'''
##====== 메인 끝 ======##