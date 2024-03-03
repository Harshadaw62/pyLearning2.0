# try :
#     # Try this code , if error
# except:
#     # Excute me if try has some error

# try:
#     c = 100/0

# Only Try is not supported!
# SyntaxError: expected 'except' or 'finally' block

print("----------------------")

# try, except and finally
# multiple exception
try:
    num1 = int(input("Enter a Number 1\n"))
    num2 = int(input("Enter a Number 2\n"))
    result = num1 / num2
except ValueError as v:
    print(v)
except ZeroDivisionError as z:
    print(z)
else:
    print(f"Result {result}")
finally:
    print("I will be executed anyhow!!")

# ValueError: invalid literal
# Zero Div
