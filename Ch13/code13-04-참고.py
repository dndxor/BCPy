import matplotlib.pyplot as plt

x = ['a', 'b', 'c', 'd', 'e']
y = [10, 30, 50, 70, 90]
z = [1, 3, 5, 7, 9]

'''
plt.subplot(2, 1, 1)
plt.plot(x, y)

plt.subplot(2, 1, 2)
plt.plot(x, z)

'''
plt.figure(1)
plt.plot(x, y)
plt.figure(2)
plt.plot(x, z)

plt.show()
