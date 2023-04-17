import time

str = "Python Programming"
slen = len(str)

#문자열 배열로 출력(좌, 우로 흐름 이동)
while True:
    for i in range(slen):
        for j in range(i, slen):
            print("%c" % str[j], end='')
        time.sleep(0.5)
        for j in range(i, slen):
            print("\b", end='')

    for i in range(slen):
        for j in range(slen-i-1, slen):
            print("%c" %str[j], end='')
        time.sleep(0.5)
        for j in range(slen-i-1, slen):
            print("\b", end='')
print()
