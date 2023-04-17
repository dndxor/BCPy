import time
sec = int(input("몇 초? "))

for i in range(sec, 0-1, -1) :
    print("%02d:" %i, end='')

    if i == sec:
        print("00", end='')
        time.sleep(0.1)
        print("\b\b", end='')
        print("\b\b\b", end='')
        continue

    for j in range(9, 0-1, -1) :
        print("%02d" %j, end='')
        time.sleep(0.1)
        print("\b\b", end='')
    print("\b\b\b", end='')
print("00:00")
