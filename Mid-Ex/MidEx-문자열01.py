str = "Python Programming"
slen = len(str)
print(slen)

#문자열 배열로 출력(순방향)
for i in range(slen):
    print("%c" %str[i], end='')
print()

#문자열 배열로 출력(역방향)
for i in range(slen-1, 0-1, -1):
    print("%c" %str[i], end='')
print()
