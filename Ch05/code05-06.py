temp = int(input("오늘 기온을 입력하세요 : "))
print("오늘 기온은 %d도입니다." % temp)

if temp < 24 :
    print("긴바지를 입으세요.")
    if temp < 10 :
        print("외투도 입는 게 좋겠네요.")
else :      #기온이 24도 이상인 경우
    print("반바지를 입으세요.")
