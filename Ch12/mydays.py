from datetime import *

def get_today() :
    today = datetime.today()
    return today.year, today.month, today.day

def str_to_date(s) :
    try :
        y = int(s[:4])
        m = int(s[4:6])
        d = int(s[6:])
    except :
        print("날짜 입력 오류")
        return -1
    else :
        return datetime(y, m, d)

def calc_days(date) :
    days = hours = 0
    if str_to_date(date) != -1 :
        result = str_to_date(date) - datetime.today()
        days = result.days
        hours = result.seconds//3600
    
    return days, hours
