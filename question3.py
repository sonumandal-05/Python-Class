# Take a list from the user for following task:
#     1.ask the number of elements
#     print the list
#     reverse the list
# modify :- number and character both are allowed in the list



x = int(input("Enter the number of elements \n: "))
l = []
for i in range(x):
    choice = (input("Type 'n' for number and 'c' for character \n: "))
    if choice == 'n':
        l.append (int(input("Enter the number \n: ")))
    else:
        l.append (input("Enter the character \n: "))
print(l)
print(l.reverse())
