import time
n = 10

for i in range(1, n+1) :
    print("%02d:" %i)
    for j in range(1, n+1) :
        print("%02d" %j)
        time.sleep(0.1)
        print("\b\b")
    time.sleep(0.1)
    print("\n")
