def solution(picks, minerals):
    mineral_values = {"diamond": 25, "iron": 5, "other": 1}
    m_values = [mineral_values.get(i, 1) for i in minerals[:5*sum(picks)]]
    m_groups = [m_values[i*5:(i+1)*5] for i in range((len(m_values)+4)//5)]

    m_groups.sort(key=sum, reverse=True)

    answer = 0

    for i in range(len(picks)):
        while picks[i] > 0 and m_groups:
            if i == 0:
                answer += len(m_groups[0])
            elif i == 1:
                answer += sum(j//5 if j > 1 else j for j in m_groups[0])
            else:
                answer += sum(m_groups[0])

            picks[i] -= 1
            m_groups.pop(0)

    return answer