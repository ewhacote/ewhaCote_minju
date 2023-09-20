def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)

def solution(W, H):
    total_squares = W * H
    cut_squares = W + H - gcd(W, H)
    result = total_squares - cut_squares
    return result