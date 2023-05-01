## 가장 작은 값을 찾아 위치 바꾸기 (2)
alist = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]
print(alist)
#Selection Sort (오름차 순)
for s in range(len(alist)):
    minx = s	#최소값 항목 index를 교환 기준값 index로 시작
    for i in range(s+1, len(alist)):
        if alist[i] < alist[minx]:
            minx = i
    alist[s], alist[minx] = alist[minx], alist[s]
print(alist)