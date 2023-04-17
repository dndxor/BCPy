import time
sec = int(input("몇 초? "))

print("%02d:00" %sec, end='')
time.sleep(0.1)
print("\b\b", end='')
for i in range(sec-1, 0-1, -1) :
    print("\b\b\b", end='')
    print("%02d:" %i, end='')
    for j in range(9, 0-1, -1) :
        print("%02d" %j, end='')
        time.sleep(0.1)
        print("\b\b", end='')
    time.sleep(0.1)
print("00")
