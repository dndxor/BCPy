x = 0

while True:
    x = x + 1
    if x >= 20:     # 20 이상이 되면 반복문 종료
        break
    if x % 3 == 0:  # 3의 배수일 때는 출력하지 않고 조건식 검사로 이동
        continue
    print(x, end = ' ')  # 20보다 작고 3의 배수가 아닐 때만 실행
print()
x = 0
while True:
    x = x + 1
    if x >= 20:  # 20 이상이 되면 반복문 종료
        break
    if (x % 3) != 0:  # 3의 배수일 때는 출력하지 않고 조건식 검사로 이동
        print(x, end=' ')  # 20보다 작고 3의 배수가 아닐 때만 실행
print()
x = 0
while x < 19:
    #if x >= 19:
    #    break
    x = x + 1
    if (x % 3) != 0:
        print(x, end=' ')

