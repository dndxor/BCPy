## 리스트 사례
l_scr = [78, 85, 68, 90, 58]

sum = 0
len_item = len(l_scr)
for i in range(len_item):
    sum += l_scr[i]
avg = sum / len_item

print(sum, avg)