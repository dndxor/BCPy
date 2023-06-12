import matplotlib.pyplot as plt

x = ['choi', 'han', 'jung', 'kim', 'lee']
y = [93, 67, 90, 78, 80]

plt.title('Scores of Students')
plt.xlabel('Stduent')
plt.ylabel('Score')
plt.grid() # 눈금선
plt.scatter(x, y, c='red', s=100, marker='>')
plt.show()
