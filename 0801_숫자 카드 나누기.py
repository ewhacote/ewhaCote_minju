import math

def solution(a, b):
    gcd_a = a[0]
    gcd_b = b[0]

    for i in range(len(a)):
        gcd_a = math.gcd(gcd_a, a[i])
        gcd_b = math.gcd(gcd_b, b[i])

    is_common_gcd_a = 1
    is_common_gcd_b = 1
    for i in range(len(a)):
        if a[i] % gcd_b == 0:
            is_common_gcd_a = 0
        if b[i] % gcd_a == 0:
            is_common_gcd_b = 0

    if is_common_gcd_a == 0 and is_common_gcd_b == 0:
        return is_common_gcd_a
    else:
        return max(gcd_a, gcd_b)
