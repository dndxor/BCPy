import matplotlib.pyplot as plt
import random

x = ['a', 'b', 'c', 'd', 'e']
y = [10, 30, 50, 70, 90]
z = random.sample(range(0, 100), 5)

plt.plot(x, y, label='diagonal', marker='o')
plt.plot(x, z, label='random', c='red', linestyle='dashed', marker='s')
#plt.plot(x, z, 'r--s', label='random')  # red+dash+square

plt.legend() # 그래프의 모양에 따라 자동으로 범례 위치 설정
plt.show()

#plt.plot(x, y, label='normal', color='red', marker='o', markerfacecolor='blue', markersize=10) # 색상
