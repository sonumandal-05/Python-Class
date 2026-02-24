x = int(input("Enter your age: "))
y = input("Do you have a ticket? (yes/no): ")
if x >= 18:
  print("You are an adult.")
  if y == "yes":
    print("You are Eligible to Enter the hall.")
else:
    print("You are not Eligible to Enter the hall.")
