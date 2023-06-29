//꼭 다시 풀어보기!!

def solution(plans):
    answer = []
    plans.sort(key=lambda x: x[1])
    paused_tasks = []

    while plans:
        if len(plans) > 1:
            name1, start1, playtime1 = plans[0]
            name2, start2, playtime2 = plans[1]
            t1 = int(start1[:2]) * 60 + int(start1[3:])
            t1_end = t1 + int(playtime1)
            t2 = int(start2[:2]) * 60 + int(start2[3:])
            if t1_end > t2:  # 새로운 일이 들어옴, 현재 작업 중단
                paused_tasks.append([t1_end - t2, name1])
                plans.pop(0)
            else:  # 진행중인 과제를 끝냄
                answer.append(name1)
                plans.pop(0)
                temp = t2 - t1_end
                while paused_tasks:
                    if paused_tasks[-1][0] <= temp:  # 중단된 작업 다시 시작
                        temp -= paused_tasks[-1][0]
                        answer.append(paused_tasks.pop()[1])
                    else:
                        paused_tasks[-1][0] -= temp
                        break
        else:
            answer.append(plans.pop(0)[0])

    return answer + list(map(lambda x: x[1], paused_tasks[::-1]))
