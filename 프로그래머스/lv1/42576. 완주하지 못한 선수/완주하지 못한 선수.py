def solution(participant, completion):
    
    dict = {}
    hash_value = 0
    for i in participant:
        dict[hash(i)] = i
        hash_value += hash(i)
    
    for j in completion:
        hash_value -= hash(j)
        
    answer = dict[hash_value]
    return answer