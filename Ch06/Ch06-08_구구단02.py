for dan in range(2, 10) :
    print("  <%d단>" % dan, end='\t\t  ')
print()

for i in range(1, 9+1):             #곱 수(1~9)
    for dan in range(2, 9+1) :      #단 반복
        print("%d x %d = %2d \t" %(dan, i, dan * i), end=' ')
    print()

