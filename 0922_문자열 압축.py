def solution(s):
    min_length = len(s)

    for size in range(1, len(s) // 2 + 2):
        compressed = ''
        count = 1
        prev = s[:size]

        for i in range(size, len(s) + size, size):
            current = s[i:i + size]
            if prev == current:
                count += 1
            else:
                compressed += (str(count) if count > 1 else '') + prev
                prev = current
                count = 1

        compressed += (str(count) if count > 1 else '') + prev
        min_length = min(min_length, len(compressed))

    return min_length
