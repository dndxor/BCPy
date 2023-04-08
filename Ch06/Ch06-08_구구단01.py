
for dan in range(2, 9+1):      #단 반복
    print("  <%d단>" % dan)
    for i in range(1, 9+1):      #곱 수(1~9)
        print("%d x %d = %2d" % (dan, i, dan * i))
    print()
