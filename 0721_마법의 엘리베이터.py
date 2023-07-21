def solution(storey):
    stor = str(storey)
    result = 0
    i = len(stor) - 1
    while i >= 0:
        digit = 10 ** (len(stor) - 1 - i) # 단위
        diff = 10 - int(stor[i]) if int(stor[i]) >= 5 else int(stor[i]) # 더 적은 차이값 이용
        result += diff 
        inc, dec = str(int(stor) + diff * digit), str(int(stor) - diff * digit)
        if stor[i] == '5':
            if i - 1 >= 0 and int(stor[i - 1]) >= 5:
                stor = inc 
            else:
                stor = dec
        elif int(stor[i]) > 5:
            stor = inc
            if len(stor) > len(str(storey)):
                i += 1
        else:
            stor = dec 
        i -= 1
    return result
