def solution(s):
    x_count = 0
    nox_count = 0
    result=0
    strlen = len(s)
    for i in range(strlen):
        
        if x_count == nox_count:
            first = s[i]
            x_count = 0
            nox_count = 0
            result+=1
            
        if first == s[i]:
            x_count+=1
        else:
            nox_count+=1
            
        
            

        
    
    answer = result
    return answer