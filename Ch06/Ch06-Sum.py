in1 = int(input("시작 숫자(정수) 입력 : "))
in2 = int(input("끝 숫자(정수) 입력 : "))

if in1 > in2 :
    in1, in2 = in2, in1

sum = 0
##whilw문 사용
i = in1
while i <= in2 :
    sum += i
    i += 1
print(">%d에서 %d까지의 합은 : %d" %(in1, in2, sum))

 
sum = 0
##for문 사용
for i in range(in1, in2+1, 1) :
    sum += i
print(">%d에서 %d까지의 합은 : %d" %(in1, in2, sum))
