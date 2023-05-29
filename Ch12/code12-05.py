# 기념일 찾기

from datetime import *

today = date.today()

print("오늘부터 몇 일 후의 날짜를 알고 싶나요?")
period = int(input("일 수 입력 : "))

result = today + timedelta(days=period)

print("오늘부터 {0}일 후는 {1}년 {2}월 {3}일입니다."
      .format(period, result.year, result.month, result.day))

