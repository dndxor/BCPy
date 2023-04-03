name = input("이름을 입력하세요 : ")
age = int(input("나이를 입력하세요 : "))

if age < 20 :
    print(name, "님은 청소년입니다.")
elif age < 30 :
    print(name, "님은 20대입니다.")
elif age < 40 :
    print(name, "님은 30대입니다.")
elif age < 50 :
    print(name, "님은 40대입니다.")
elif age < 60 :
    print(name, "님은 50대입니다.")
else :
    print(name, "님은 60대 이상입니다.")
