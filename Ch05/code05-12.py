age = int(input("나이를 입력하세요 : "))

print("** 추천 영화 목록 **")
if age < 20:
    print("어벤저스")
if age < 40:
    print("뮬란")
if 20 <= age < 60:
    print("테넷")
if 20 <= age < 40 or age >= 60:
    print("오!문희")
