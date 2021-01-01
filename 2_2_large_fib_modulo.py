def fib_modulo(n, m):
    """Given 2 ints: 1 <= n <= 10^17 and 2 <= m <= 10^5
    Return the modulo for division of n-th Fib by m"""
    # Function to calculate the Pisano period
    def fn_pisano_seq(y):
        """Returns an array (list) of Pisano sequence for the given y"""
        # Define 2 first Fibonacci numbers
        a = 0
        b = 1
        # Define basis Pisano sequence
        pisano_period = [0, 1]
        # Maximum Pisano period is m * 6
        # Account for range (+1) and list indexing (+1) = +2
        for j in range(2, y * 6 + 2):
            # Calculate the next Fibonacci number (starting with j == 2)
            # b is the next Fibonacci number
            a, b = b, a + b
            # Add modulo b % m to the pisano sequence
            pisano_period.append(b % m)
            # Check if current and previous moduli are not 0 and 1
            # If yes - sequence is repeating itself --> break
            if pisano_period[j] == 1 and pisano_period[j - 1] == 0:
                break
        # Return sequence without 2 last elements, since they belong to the repeated sequence
        return pisano_period[:j - 1]

    # Calculate the pisano sequence and period for the given m
    pisano_sequence_m = fn_pisano_seq(m)
    pisano_period_m = len(pisano_sequence_m)

    # Find n % m as element at index (n % pisano period of m)
    return pisano_sequence_m[n % pisano_period_m]


print((fib_modulo(47905881698199969, 76940)))
