import time
sec = 10

for i in range(sec) :
    print("%02d:" %i, end='')
    for j in range(10) :
        print("%02d" %j, end='')
        time.sleep(0.1)
        print("\b\b", end='')
    print("\b\b\b", end='')
print()
