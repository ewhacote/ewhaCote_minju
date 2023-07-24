def solution(n, l, r):
    quin_l = quin(l - 1)
    quin_r = quin(r)
    count_l = decode(quin_l)
    count_r = decode(quin_r)
    return count_r - count_l

def quin(n):
    result = []
    while n > 0:
        n, mod = divmod(n, 5)
        result.append(mod)
    return result[::-1]

def decode(quinary):
    result = 0
    length = len(quinary)
    dec = [0, 1, 2, 2, 3]
    for i, x in enumerate(quinary):
        exponent = length - i - 1
        result += (4**exponent) * dec[x]
        if x == 2:
            break    
    return result
