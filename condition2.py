x = int(input("Enter your age: "))
y = input("Do you have a ticket? (yes/no): ")
if x >= 18 and y == "yes":
    print("You are an adult and have a ticket.")
else:
    print("You are either a minor or do not have a ticket.")