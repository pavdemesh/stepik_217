def gcd(a, b):
    """a >= 1 and b <= 2 * 10^9"""
    if a == 0:
        return b
    elif b == 0:
        return a
    elif a >= b:
        return gcd(a % b, b)
    else:
        return gcd(a, b % a)


print(gcd(3918848, 1653264))