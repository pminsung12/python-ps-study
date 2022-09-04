def solution(lottos, win_nums):
    answer = []
    chk=0
    zero=0
    cnt=0
    for i in range(6):
        chk=0
        if lottos[i]==0:
            zero+=1
            
        for j in range(6):
            if lottos[i] == win_nums[j]:
                chk=1
        if chk:
            cnt +=1
    
    for i in range(2):
        cnt+=zero
        if i ==1:
            cnt=cnt-zero*2
        
        if cnt ==6:
            res=1
        elif cnt==5:
            res=2
        elif cnt==4:
            res=3
        elif cnt==3:
            res=4
        elif cnt==2:
            res=5
        else:
            res=6
        answer.append(res)
    
    
    return answer