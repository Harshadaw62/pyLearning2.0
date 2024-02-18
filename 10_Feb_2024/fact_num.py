num = int(input("Enter the number you want factorial: "))
fact = 1
if num<=0:
    print("Factorial of negative number not possible")
elif num==0:
    print("Factorial of 0 is 1")
else:

    for i in range(1, num + 1):
        fact = fact * i
print(f"Factorial of number {num} is {fact}")
