##[실습] n의 m승 결과를 반환하는 재귀함수  >> Ch10-nPowerM.py
def powers(n, m):  # 재귀 호출 함수
    # print(">Call %d" %m)
    if m > 1:  # 재귀 호출 조건
        result = powers(n, m - 1) * n
        # print(">Return %d" %result)
        return result  # 재귀 호출: 호출 조건 값(num)의 변화 필수
    else:
        return n  # 재귀 호출 종료 후 복귀


inlist = [x for x in input(">(n의 m승)의 n m 입력? ").split()]
n, m = int(inlist[0]), int(inlist[1])
result = powers(n, m)
print(">>", result)