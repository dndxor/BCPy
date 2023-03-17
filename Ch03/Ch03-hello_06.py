
'''
import os           #os.system() 함수를 사용하기 위한 설정

print("Hello~")     #실행할 코드

os.system('Pause')  #실행 창을 닫지 않도록 추가한 문장
'''



## hello_00
print("Hello~")   #실행할 코드

# hello_06
while True :
    '''
    ## hello_01
    print("당신의 이름은요?")
    print("아~ ㅇㅇㅇ씨군요.")
    print("ㅇㅇㅇ씨 반가워요.")
    '''

    '''
    ## hello_02
    print("당신의 이름은요?")
    input("<이름 입력> ")
    print("아~ ㅇㅇㅇ씨군요.")
    print("ㅇㅇㅇ씨 반가워요.")
    '''

    ## hello_03
    print("당신의 이름은요?")
    name = input("<이름 입력> ")        ##변수(variable)를 통해 잠시(메모리에) 기억

    print("아~ %s씨군요." % name)
    print("%s씨 반가워요." % name)

    ## hello_04
    age = int(input("<나이 입력> "))      ##변수의 자료형이 다르므로 형식 변환
    print("아~ %d살..." % age)
    myage = 30
    print("나하고 %d살 차이가 나네요." % abs(myage - age))   ##연산

    '''
    ## hello_05
    if myage > age:
        print("그럼 내가 위네요.")
    if myage < age:
        print("그럼 당신이 위네요.")
    if myage == age:
        print("그럼 동갑이네요.")
    '''

    ## hello_05-1
    if myage > age:
        print("그럼 내가 위네요.")
    elif myage < age:
        print("그럼 당신이 위네요.")
    else :
        print("그럼 동갑이네요.")

    ## hello_06
    yn = input(">>그만 하려면 x를 입력? ")
    if yn == 'x' or yn == 'X':
        break


## input()           #실행 창을 닫지 않도록 추가한 문장
