in1 = int(input(">정수 입력(1) : "))
in2 = int(input(">정수 입력(2) : "))
'''
if in1 >= in2 :
    print(">>큰 수는 %d" %in1)
else :
    print(">>큰 수는 %d" %in2)
'''

##변수 사용
if in1 >= in2 :
    max = in1
else :
    max = in2
print(">>큰 수는 %d" %max)

##3항연산 사용
max = in1 if in1 >= in2 else in2
print(">>큰 수는 %d" %max)
