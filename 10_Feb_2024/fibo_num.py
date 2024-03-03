last_pos = int(input("Enter last position for Fibonacci: "))
a, b = 0, 1
while a < last_pos:
    print(a, end=" ")
    a, b = b, a + b


def generate_fibonacci(limit):
    # Initialize the first two Fibonacci numbers
    fibonacci_sequence = [0, 1]

    # Generate Fibonacci numbers until the limit is reached
    while fibonacci_sequence[-1] + fibonacci_sequence[-2] <= limit:
        next_fibonacci = fibonacci_sequence[-1] + fibonacci_sequence[-2]
        fibonacci_sequence.append(next_fibonacci)

    return fibonacci_sequence

# Example usage:
limit = int(input("\nEnter the limit for Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci(limit)
print("Fibonacci sequence up to", limit, ":", fibonacci_sequence)