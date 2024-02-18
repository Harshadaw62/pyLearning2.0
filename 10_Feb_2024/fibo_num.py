last_pos = int(input("Enter last position for Fibonacci: "))
a, b = 0, 1
while a < last_pos:
    print(a, end=" ")
    a, b = b, a + b
