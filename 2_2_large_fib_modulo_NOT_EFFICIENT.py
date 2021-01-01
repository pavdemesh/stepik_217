# This Solution works only with small numbers
def fib_modulo(n, m):
    """Given 2 ints: 1 <= n <= 10^17 and 2 <= m <= 10^5
    Return the modulo for division of n-th Fib by m"""
    # Define fibonacci function:
    def fn_fib_seq(x):
        """Returns an array (list) of Fibonacci numbers from 0 up to n"""
        arr = [0, 1]
        for i in range(2, x + 1):
            i_th_number = arr[i - 1] + arr[i - 2]
            arr.append(i_th_number)
        return arr

    # Function to calculate the Pisano period
    def fn_pisano_seq(y):
        """Returns an array (list) of Pisano sequence for the given y"""
        fib_arr = fn_fib_seq(y * 6 + 2)
        pisano_period = [0, 1]
        for j in range(2, y * 6 + 2):
            modulo = fib_arr[j] % m
            pisano_period.append(modulo)
            if pisano_period[j] == 1 and pisano_period[j - 1] == 0:
                break
        return pisano_period[:j - 1]

    pisano_sequence_m = fn_pisano_seq(m)
    pisano_period_m = len(pisano_sequence_m)

    return pisano_sequence_m[n % pisano_period_m]


print((fib_modulo(47905881698199969, 76940)))
