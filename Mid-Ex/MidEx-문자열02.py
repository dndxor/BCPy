str = "Python Programming"
slen = len(str)
print(slen)

#문자열 배열로 출력(좌로 이동)
for i in range(slen):
    for j in range(i, slen):
        print("%c" %str[j], end='')
    print()
print()

#문자열 배열로 출력(우로 이동)
for i in range(slen):
    for j in range(slen-i-1, slen):
        print("%c" %str[j], end='')
    print()
print()

