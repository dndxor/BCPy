for i in range(1, 5+1, 1):     #행 제어
    for j in range(1, i+1, 1):  #열 제어
        print('*', end='')
    print()

## 5단 별탑 쌓기
for i in range(1, 5+1, 1):     #행 제어
    for j in range(5, i-1, -1):  #열 제어
        print('*', end='')
    print()

for i in range(1, 5+1, 1):         #행 제어
    for j in range(6-i, 0, -1):      #열 제어
        print('*', end='')
    print()

## 5단 별탑 쌓기
for i in range(5, 0, -1):     #행 제어
    for j in range(1, i+1, 1):  #열 제어
        print('*', end='')
    print()