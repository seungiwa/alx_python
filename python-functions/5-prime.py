def is_prime(number):
    # Numbers less than 2 are not prime
    if number < 2:
        return False

    # Check for divisibility from 2 up to the square root of the number
    for divisor in range(2, int(number**0.5) + 1):
        if number % divisor == 0:
            return False

    return True