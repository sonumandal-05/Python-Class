x = int(input("Enter a number:"))
num=0
for i in range(1,x+1):
    if x%i==0:
        num=num+1
if num==2:  
    print("The number is prime")
else:
    print("The number is not prime")