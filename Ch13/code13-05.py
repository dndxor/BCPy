# 연도별 교통사고통계 그래프 그리기

import matplotlib.pyplot as plt
import csv

f = open("교통사고통계.csv", "r")
data = csv.reader(f)
next(data) # 제목 행 건너뛰기
x = []
y = []
for row in data:
    x.append(row[0])
    y.append(int(row[1]))
f.close()

plt.rcParams['font.family']='Malgun Gothic'
plt.figure(figsize=(12, 5), facecolor='lightyellow')
plt.bar(x, y, color="darkgreen")
plt.xlabel('Year')
plt.ylabel('Number of accidents')
plt.title('연도별 교통사고통계')
plt.show()
