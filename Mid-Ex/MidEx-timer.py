import time
n = 10

for i in range(1, n+1) :
    print("%02d:" %i, end='')
    for j in range(1, n+1) :
        print("%02d" %j, end='')
        time.sleep(0.1)
        print("\b\b", end='')
    time.sleep(0.1)
    print("\b\b\b", end='')
print()
