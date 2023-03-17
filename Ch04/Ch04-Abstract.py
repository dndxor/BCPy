def check_age(myage, age) :
    if myage > age :
        print("그럼 내가 위네요.")
    elif myage < age :
        print("그럼 당신이 위네요.")
    else :
        print("그럼 동갑이네요.")

while True :
    age = int(input("<나이 입력> "))
    print("아~ %d살..." % age)
    myage = 30
    print("나하고 %d살 차이가 나네요." % abs(myage - age))

    check_age(myage, age)

    yn = input(">>그만 하려면 x를 입력? ")
    if yn == 'x' or yn == 'X' :
        break
