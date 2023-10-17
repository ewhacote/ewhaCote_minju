def solution(people, limit):
    people.sort()
    count = 0
    i, j = 0, len(people) - 1

    while i <= j:
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
        count += 1

    return count