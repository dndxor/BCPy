#[함수] 큰거 반환
def imax(a, b):
    if a > b:
        return a
    else:
        return b

in1 = int(input(">정수 입력(1) : "))
in2 = int(input(">정수 입력(2) : "))
in3 = int(input(">정수 입력(3) : "))

max = in1
max = imax(max, in2)
max = imax(max, in3)
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
