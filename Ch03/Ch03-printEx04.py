##[Ch03-printEx05.py] *탑 그리기

print(" " * 4, "*" * 1)
print(" " * 3, "*" * 2)
print(" " * 2, "*" * 3)
print(" " * 1, "*" * 4)
print(" " * 0, "*" * 5)

for i in range(1, 5+1, 1):
    print(" " * (5-i), "*" * i)

n = int(input("층 수(0~100): "))
for i in range(1, n+1, 1):
    print(" " * (n-i) + "*" * i)


