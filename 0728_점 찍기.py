def solution(k, d):
    count = 0
    coordinates = []
    idx = 0
    while (idx * k) ** 2 <= d ** 2:
        coordinates.append(idx * k)
        idx += 1

    high = len(coordinates) - 1
    low = 0
    while low < len(coordinates):
        if coordinates[low] ** 2 + coordinates[high] ** 2 > d ** 2:
            high -= 1
        else:
            count += (high + 1)
            low += 1
    return count
