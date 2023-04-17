sum = 0
scnt = 0
xcnt = 0
scr = 0

while scr >= 0:
    scr = int(input("과목 점수? "))
    if scr < 0 or scr > 100:
        break
    if scr < 40:
        xcnt += 1
    scnt += 1
    sum += scr

if scnt > 0:
    avg = sum / scnt
    if avg < 60 or xcnt > 0:
        result = "불합격"
    else:
        result = "합격"
    print(avg)
    print(result)