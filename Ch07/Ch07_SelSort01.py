## 가장 작은 값을 찾아 위치 바꾸기 (1)
alist = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]
print(alist)

minx = 0	#최소값 항목 index
for i in range(1, len(alist)):
    if alist[i] < alist[minx]:
        minx = i
alist[0], alist[minx] = alist[minx], alist[0]    #항목 교환
print(alist)