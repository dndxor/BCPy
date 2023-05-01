## 튜플과 리스트의 차이 > read
l_scr = [78, 85, 68, 90, 58]  # 리스트 구조

sum = 0
len_item = len(l_scr)
for i in range(len_item):
    l_scr[i] += 5

for x in l_scr:
    sum += x
avg = sum / len_item

print(sum, avg)