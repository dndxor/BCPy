in1 = int(input(">정수 입력(1) : "))
in2 = int(input(">정수 입력(2) : "))
in3 = int(input(">정수 입력(3) : "))
'''
if in1 >= in2 :
    if in1 >= in3 :
        print(">>큰 수는 %d" %in1)
    else :
            print(">>큰 수는 %d" %in3)
else :
    if in2 >= in3 :
        print(">>큰 수는 %d" %in2)
    else :
        print(">>큰 수는 %d" %in3)
'''
##변수 사용
max = in1
if max < in2:
    max = in2

if max < in3:
    max = in3
print(">>큰 수는 %d" % max)
'''
##3항연산 사용(1)
max = (in1 if in1 >= in2 else in2) if ((in1 if in1 >= in2 else in2) > in3) else in3
print(">>큰 수는 %d" %max)

##3항연산 사용(2)
max = in1
max = (in2 if in2 > max else max) if ((in2 if in2 > max else max) > in3) else in3
print(">>큰 수는 %d" %max)
'''
