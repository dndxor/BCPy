temp = int(input("기온 : "))
dust = int(input("미세먼지 : "))

if temp > 0 :
    print("오늘 기온은 영상 %d 도입니다." % temp)
else :
    print("오늘 기온은 영하 %d 도입니다." % temp)

print("미세먼지 농도는 %d 마이크로그램으로," % dust, end=' ')
    
if dust > 80:
    print("나쁨 수준입니다. 마스크를 착용하세요.")
else :
    print("쾌적합니다.")
