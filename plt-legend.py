import matplotlib.pyplot as plt

x=[1, 2, 3, 4, 5]
y1=[2, 3, 5, 7, 11]
y2=[1, 4, 6, 8, 10]
plt.plot(x, y1, label='Data vs Output', color='blue', marker='o', linestyle='-')
plt.plot(x,y2, label='Data vs Output2', color='red', marker='x', linestyle='--')
plt.xlabel('Data')
plt.ylabel('Output')
plt.title('Line Graph with Legend')
plt.legend()
plt.grid()
plt.show()