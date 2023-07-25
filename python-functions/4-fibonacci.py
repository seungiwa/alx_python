def fibonacci_sequence(n):
    # Initialize the list to store the Fibonacci numbers
    fib_sequence = []

    # First two numbers of the Fibonacci sequence
    a, b = 0, 1

    # Generate the Fibonacci sequence up to the nth number
    for _ in range(n):
        # Append the current number (a) to the list
        fib_sequence.append(a)
        # Calculate the next Fibonacci number by adding the previous two numbers
        a, b = b, a + b

    return fib_sequence
