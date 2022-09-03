from collections import defaultdict
def solution(id_list, report, k):
    #중복제거
    report=list(set(report))
    
    answer = []
    user=defaultdict(set)
    cnt=defaultdict(int)
    
    for i in range(len(report)):
        x,y=report[i].split(' ')
        user[x].add(y)
        cnt[y]+=1
        
    for i in id_list:
        res=0
        for u in user[i]:
            if cnt[u]>=k:
                res+=1
        answer.append(res)
    
    return answer


"""

# 시간초과 되지는 않았지만 아슬아슬

def solution(id_list, report, k):
    #중복제거
    report=list(set(report))
    
    answer = []
    dic1={}
    dic2={}
    reported=[]
    for id in id_list:
        dic1[id]=0
        dic2[id]=0
    
    # 신고당한 횟수
    for i in range(len(report)):
        s=report[i].split(' ')[1]
        dic1[s]+=1
    
    # 신고당한 사람들
    for i,j in dic1.items():
        if j>=k:
            reported.append(i)
    
    for i in range(len(report)):
        s=report[i].split(' ')[1]
        if s in reported:
            t=report[i].split(' ')[0]
            dic2[t]+=1

            
    for k,v in dic2.items():
        answer.append(v)
    return answer
    
"""