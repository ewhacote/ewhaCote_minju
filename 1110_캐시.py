def solution(cacheSize, cities):
    answer = 0
    memolist=[]
    
    if cacheSize==0:
        return len(cities)*5

    else:
        cities[0]=cities[0].upper()
        memolist.append(cities[0])
        answer+=5
        
        for i in range(1,len(cities)):
            cities[i]=cities[i].upper()
            check=True
            
            for j in range(len(memolist)):
                if memolist[j]==cities[i]:
                    memolist.remove(cities[i])
                    memolist.append(cities[i])
                    answer+=1
                    check=False # 중복된거 있음!
                    break
            
            if  check:
                answer+=5
                if len(memolist)==cacheSize:
                    memolist.pop(0)
                memolist.append(cities[i])
                
                
    
    return answer