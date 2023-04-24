import calendar
##[함수] 년,월을 받아 월의 마지막 일자 반환
def get_month_end(y, m):
    val = calendar.monthrange(y, m)
    return val[1]
##[함수] 년,월을 받아 1일의 요일 순서번호 반환(0이 월)
def get_month_weekday(y, m):
    val = calendar.monthrange(y, m)
    return val[0]

##[Main]
year = int(input("년도(4자리): "))
month = int(input("월(2자리): "))

wday = get_month_weekday(year, month)  #해당 년도/달의 1일의 요일 순서 값
mend = get_month_end(year, month)   #해당 년도/달의 마지막 날의 값

print(wday)
print(mend)
