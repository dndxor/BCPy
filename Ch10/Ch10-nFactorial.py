def mul(num):  # 재귀 호출 함수
    print(">> Call %d" % num)
    if num > 1:  # 재귀 호출 조건
        result = num * mul(num - 1)  # 재귀 호출: 호출 조건 값(num)의 변화 필수
        print("<< Return %d" % result)
        return result
    else:
        return 1  # 재귀 호출 종료 후 복귀

n = int(input(">누적 곱할 끝 수? "))
result = mul(n)
print(">>", result)
