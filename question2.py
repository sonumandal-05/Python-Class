# Take a list from the user for following task:
#     1.ask the number of elements
#     print the list
#     reverse the list



x = int(input("Enter the number of elements \n: "))
l = []
for i in range(x):
    l.append (int(input("Enter the element \n: ")))
print(l)
print(l.reverse())
print(l[::-1])    