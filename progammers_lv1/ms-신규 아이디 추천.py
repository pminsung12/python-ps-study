def solution(new_id):
    answer = ''
    #step1
    new_id = new_id.lower()
    print(answer)
    #step2
    for id in new_id:
        if id.islower() or id.isdigit() or id in ['-', '_', '.']:
            answer += id
    print(answer) 
    #step3
    while '..' in answer:
        answer = answer.replace('..', '.')
    print(answer)
    #step4
    answer=answer.lstrip('.')
    answer=answer.rstrip('.')
    print(answer)
    #step5
    if not answer:
        answer = "a"
    print(answer)    
    #step6
    if len(answer)>=16:
        answer=answer[0:15]
        answer=answer.rstrip('.')
    print(answer)
    #step7
    if len(answer)<=2:
        ss=answer[-1]
        while(len(answer)<3):
            answer+=ss
    
    
    return answer