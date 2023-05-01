##모듈 임포트
import random
import os

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

def left(r, c):
    global puzzle, col
    if col <= c+1 :
        return 1
    else :
        puzzle[r][c+1], puzzle[r][c] = puzzle[r][c], puzzle[r][c+1]
        return 0

def right(r, c):
    global puzzle
    if 0 > c-1 :
        return 1
    else :
        puzzle[r][c-1], puzzle[r][c] = puzzle[r][c], puzzle[r][c-1]
        return 0

def up(r, c):
    global puzzle, row
    if row <= r+1 :
        return 1
    else :
        puzzle[r+1][c], puzzle[r][c] = puzzle[r][c], puzzle[r+1][c]
        return 0

def down(r, c):
    global puzzle
    if 0 > r-1 :
        return 1
    else :
        puzzle[r-1][c], puzzle[r][c] = puzzle[r][c], puzzle[r-1][c]
        return 0

##====== 메인 시작 ======##
## 변수 초기화
col = int(input("열 개수는? "))
row = col

rand_puzzle()
prt_puzzle()

#print("r: %d, c: %d" %(r, c))

while True :
    zero_seq = find_zero()
    r = zero_seq // row  # zero 위치 행
    c = zero_seq % row  # zero 위치 열
    key = input("a(좌) w(상) s(하) d(우) > ")
    if key == 'a' :
        left(r, c)
    elif key == 'd' :
        right(r, c)
    elif key == 'w' :
        up(r, c)
    elif key == 's' :
        down(r, c)
    elif key == '0' :
        break
    else:
        print("??잘못된 키 값입니다!")

    os.system('cls')    #os.system('cls' if os.name == 'nt' else 'clear')
    prt_puzzle()

##====== 메인 끝 ======##

