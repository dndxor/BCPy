## 5단 숫자탑 쌓기
for i in range(1, 5+1, 1):     #행 제어
    for j in range(1, i+1, 1):  #열 제어
        print(i, end='')
    print()

## 5단 역숫자탑 쌓기 (11111)
for i in range(1, 5+1, 1):     #행 제어
    for j in range(0, (5-i)+1, 1):  #열 제어
        print(i, end='')
    print()
