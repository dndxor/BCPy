alist = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]
print(alist)
#Bubble Sort (내림차 순)
for s in range(len(alist), 0, -1):  #가장 작은 값부터 오른쪽 끝에 배치하고자 하는 오른쪽 제어
    for i in range(s-1):
        if alist[i] < alist[i+1]:   #맨 왼쪽부터 다음과 값 비교
            alist[i], alist[i+1] = alist[i+1], alist[i]   #위치 교환
        print(alist)
print(alist)