## 리스트 사례
l_scr = [78, 85, 68, 90, 58]  #리스트 구조

sum = 0
len_item = len(l_scr)
for x in l_scr:
    sum += x
avg = sum / len_item

print(sum, avg)