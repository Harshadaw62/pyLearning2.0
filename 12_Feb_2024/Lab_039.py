# # Factorial
# n = 5
# 5*4*3*2*1 = 120
# n = 3
# 3*2*! => 6

number = int(input("Enter the Fac number\n"))
fact = 1
if number < 0:
    print("Fact not possible")
elif number == 0:
    print("Fact - ", 1)
else:

    for i in range(1, number + 1):
        fact = fact * i

    print("Fact ->>", fact)