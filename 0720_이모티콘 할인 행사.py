from itertools import product

def get_price(emoticons, ratio, user_rate, max_cost):
    total_cost = sum([emoticons[i] * (100 - ratio[i]) // 100 for i in range(len(emoticons)) if ratio[i] >= user_rate])
    if total_cost >= max_cost:
        return 0, True
    else:
        return total_cost, False

def solution(users, emoticons):
    answer = []
    for ratio in product([10, 20, 30, 40], repeat=len(emoticons)):
        membership, total = 0, 0
        for user in users:
            cost, is_member = get_price(emoticons, ratio, user[0], user[1])
            if is_member:
                membership += 1
            else:
                total += cost
        answer.append([membership, total])

    answer.sort(key=lambda x: (-x[0], -x[1]))
    return answer[0]
