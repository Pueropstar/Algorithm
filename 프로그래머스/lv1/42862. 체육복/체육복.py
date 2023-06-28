def solution(n, lost, reserve):
    answer = 0
    lostlen = len(lost)
    lost.sort()
    reserve.sort()
    
    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j]:
                lost[i] = -1
                reserve[j]=-1
                answer+=1
    
    for i in range(len(lost)):
        for j in range(len(reserve)):

            if lost[i]-1 == reserve[j] or lost[i]+1 == reserve[j]:
                del reserve[j]
                answer+=1
                break
    
    answer+= n-lostlen
    return answer