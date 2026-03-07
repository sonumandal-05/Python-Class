num = int(input("Enter a number: "))
temp =0
num1=num
for i in range (len(str(num))):
    rem = num%10
    temp = temp*10 + rem
    num = num//10
print(temp) 
if temp ==num1:
   print("Number is palindrome")
else:
    print("Number is not palindrome")
