cnt = 0       # 반복횟수를 저장하기 위한 변수

for i in range(5):  # 0부터 5번 반복
    cnt += 1
    print("[%02d] i=%d" %(cnt, i), end = " ")

print("")
cnt = 0
for i in range(0, 5, 1):  # 0부터 5번 반복
    cnt += 1
    print("[%02d] i=%d" %(cnt, i), end = " ")

print("")
cnt = 0
for i in range(1, 5+1, 1):  # 1부터 5번 반복
    cnt += 1
    print("[%02d] i=%d" %(cnt, i), end = " ")
