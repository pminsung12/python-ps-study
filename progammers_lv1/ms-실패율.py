def solution(N, stages):
    answer = []
    
    tried=len(stages)
    failure={}
    for i in range(1,N+1):
        if tried!=0:
            cnt=stages.count(i)
            failure[i]=cnt/tried
            tried-=cnt
        else:
            failure[i]=0
    
    return sorted(failure, key=lambda x:failure[x], reverse=True)
