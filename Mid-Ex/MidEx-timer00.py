import time

for i in range(10) :
    print("%02d" %i, end='')
    time.sleep(0.5)
    print("\b\b", end='')
