# Take two list from the user (For numbers only) 
# Now make a list which have common number present in the two list
# print all the list

n1,n2 = map(int,input("Enter the number of elements in list 1 and list 2 \n: ").split())
l1 = []
l2 = []
l3 = []
for i in range(n1):
    l1.append (eval(input("Enter the element for list 1 \n: ")))
for i in range(n2):
    l2.append (eval(input("Enter the element for list 2 \n: ")))
print(l1)        
print(l2)
for i in l1:
    for j in l2:
        if i == j:
            l3.append(i)
print(l3)               