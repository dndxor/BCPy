dan = int(input("몇단(2~9)? "))

for i in range(1, 9+1):      #곱 수(1~9)
    print("%dx%d=%2d" % (dan, i, dan * i))

