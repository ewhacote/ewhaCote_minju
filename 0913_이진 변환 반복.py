def solution(s):
    trans_count, zero_count = 0, 0

    while s != "1":
        zero_count += s.count("0")
        s = s.replace("0", "")

        s = bin(len(s))[2:]
        trans_count += 1

    return [trans_count, zero_count]
