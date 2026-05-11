import matplotlib.pyplot as plt
data = [10, 20, 30,30,30, 40, 50,50,60]
plt.hist(data, bins=5, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram')
plt.grid(axis='y', alpha=0.75)
plt.show()