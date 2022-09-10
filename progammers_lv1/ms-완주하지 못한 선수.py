from collections import defaultdict

def solution(participant, completion):
    answer = ''
    part = defaultdict(int) # 자동으로 0으로 초기화
    for c in completion:
        part[c] +=1
    
    for p in participant:
        if p in part:
            part[p]-=1
            if part[p]<=0:
                del part[p]
            continue
        else:
            answer=p
            break
    return answer