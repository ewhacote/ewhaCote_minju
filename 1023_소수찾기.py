def solution(brown, yellow):
    def get_divisors(n):
        divisors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return divisors
    
    divisors = get_divisors(yellow)

    for width in divisors:
        height = yellow // width
        total_brown = (width + 2) * (height + 2) - yellow
        if total_brown == brown:
            return [width + 2, height + 2] if width >= height else [height + 2, width + 2]

    return []