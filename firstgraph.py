import matplotlib.pyplot as plt
x=[1, 2, 3, 4, 5]
y=[2, 3, 5, 7, 11]
plt.plot(x, y, color='red', marker='o', linestyle='--')
plt.xlabel('Data')
plt.ylabel('Output')
plt.title('Line Graph')
plt.grid()
plt.show()