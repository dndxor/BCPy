goal = int(input(">목표 값은? "))
sum = 0
num = 0
while goal > sum:
    num += 1
    sum += num
print(">>1~%d의 합: %d" %(num, sum))