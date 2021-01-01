def fib_last_digit(n):
    """Input is an int between 1 and 10^7
    Returns the last digit of the nth Fibonacci number"""
    # Define an array with last digits for the numbers 0 and 1
    arr = [0, 1]

    # Calculate last digit for the i-th element
    # Append this digit to the array of last digits
    # Last digit for Fib(2) will be appended to the list [0, 1]
    # So that the last digit for Fib(2) will be stored at index 2
    for i in range(2, n + 1):
        i_th_digit = (arr[i - 1] + arr[i - 2]) % 10
        arr.append(i_th_digit)

    return arr[n]


print(fib_last_digit(20))
