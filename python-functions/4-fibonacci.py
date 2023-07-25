def fibonacci_sequence(n):
    # Initialize the list to store the Fibonacci numbers
    fib_sequence = []

    # First two numbers of the Fibonacci sequence
    x, y = 0, 1

    # Generate the Fibonacci sequence up to the nth number
    for i in range(n):
        # Append the current number (a) to the list
        fib_sequence.append(x)
        # Calculate the next Fibonacci number by adding the previous two numbers
        x, y = y, x + y