def solution(topping):
    cnt1, cnt2 = [], []
    unique1, unique2 = set(), set()

    for t in topping:
        unique1.add(t)
        cnt1.append(len(unique1))

    for t in topping[::-1]:
        unique2.add(t)
        cnt2.append(len(unique2))

    cnt2 = cnt2[::-1]
    return sum([1 for i in range(len(cnt1) - 1) if cnt1[i] == cnt2[i + 1]])
