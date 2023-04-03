sex = input("성별 입력(f/m): ")
age = int(input("나이 입력: "))

if age >= 5:
    if sex == 'f':
        print("여탕 입장")
    else:
        print("남탕 입장")
else:
        print("아무탕 입장")
        
