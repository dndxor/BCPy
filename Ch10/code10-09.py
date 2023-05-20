# 함수를 이용한 사칙연산기

def f_add(x, y) :
    return x + y

def f_sub(x, y) :
    return x - y

def f_mul(x, y) :
    return x * y

def f_div(x, y) :
    return x / y

try :
    num1 = int(input("정수 입력 : "))
    num2 = int(input("정수 입력 : "))
    operator = int(input("연산 종류(1:덧셈 2:뺄셈 3:곱셈: 4:나눗셈) : "))
except :
    print("정수를 입력하세요.")
else :
    if 1 <= operator <= 4 :
        if operator == 1 :
            result = f_add(num1, num2)
        elif operator == 2 :
            result = f_sub(num1, num2)
        elif operator == 3 :
            result = f_mul(num1, num2)
        else :
            result = f_div(num1, num2)
        print("계산 결과 = ", result)
    else :
        print("잘못된 연산자입니다.")
        
 
