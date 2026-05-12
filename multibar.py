import matplotlib.pyplot as plt
students=['Ziyarat','Rakesh','Shoeb']
marks1=[30,40,50]
marks2=[70,80,90]
plt.bar(students, marks1, label='Marks 1', color='b')
plt.bar(students, marks2, label='Marks 2', color='r', bottom=marks1)
plt.xlabel('Students')
plt.ylabel('Marks')
plt.title('Marks of Students')
plt.legend()
plt.show()