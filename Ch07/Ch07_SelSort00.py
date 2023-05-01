## 1차원 리스트에서 가장 작은 값 찾기
alist = [4, 3, 2, 6, 1, 0, 8, 3, 6, 6, 9, 7]
print(alist)

minx = 0	#최소값 항목 index
for i in range(1, len(alist)):
    if alist[i] < alist[minx]:
        minx = i
print("[%d] %d" %(minx, alist[minx])) 