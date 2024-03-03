def fact_fun(num1):
    fact = 1
    if num1<0:
        print("Factorial of negative number not possible")
    elif num1==0:
        print("Factorial of 0 is 1")
    else:
        for i in range(1, num1 + 1):
            fact = fact * i
        print(f"factorial of {num1} is {fact}")


fact_num = int(input("Enter the number you want factorial: "))
fact_fun(fact_num)

