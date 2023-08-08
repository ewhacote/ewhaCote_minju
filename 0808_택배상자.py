def solution(order):
    assist = []  # 보조 컨테이너 벨트
    i = 1        # 메인 컨테이너 벨트 상자 번호
    cnt = 0      # 트럭에 실은 상자의 수
    
    while i <= len(order):
        if order[cnt] == i:  # 현재 상자가 다음에 실어야 할 상자라면
            cnt += 1
            i += 1
            while assist and assist[-1] == order[cnt]:  # 보조 컨테이너 벨트의 상자 검사
                assist.pop()
                cnt += 1
        else:
            assist.append(i)
            i += 1

    return cnt