# 인공지능 기상 캐스터

weekday = input("요일 : ")
weather = int(input("날씨 1(맑음), 2(흐림) : "))
temp = int(input("기온 : "))
cold = ""

if weather == 1 :
    weather = "맑습니다"
else :
    weather = "흐립니다"

if temp <= 10 :
    cold = "쌀쌀한"
else :
    cold = "따뜻한"

print("\n★오늘의 날씨★")
print("{0}요일인 오늘은 전국이 {1}. 이날 기온은 {2}도로 관측됩니다. \
{3} 출근길이 될 것으로 예상되므로 알맞은 옷차림을 미리 준비하시기 바랍니다. \
전국 대부분 지역에서 낮과 밤의 기온 차가 큰 편이므로, \
건강관리에 유의하시기 바랍니다. \
오늘 {0}요일도 편안한 하루 되시고요~".format(weekday, weather, temp, cold))
