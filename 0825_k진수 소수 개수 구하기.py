def solution(n, k):
    conv = ""
    while n:
        conv = str(n % k) + conv
        n = n // k

    segs = conv.split("0")

    cnt = 0
    for seg in segs:
        if len(seg) == 0 or int(seg) < 2:
            continue

        is_p = True
        for i in range(2, int(int(seg)**0.5) + 1):
            if int(seg) % i == 0:
                is_p = False
                break

        if is_p:
            cnt += 1

    return cnt
