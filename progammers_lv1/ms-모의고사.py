def solution(answers):
    answer = []
    one=[1,2,3,4,5]
    two=[2,1,2,3,2,4,2,5]
    three=[3,3,1,1,2,2,4,4,5,5]
    
    one_score=0
    two_score=0
    three_score=0
    for i in range(len(answers)):
        if answers[i]==one[i%5]:
            one_score+=1
        if answers[i]==two[i%8]:
            two_score+=1
        if answers[i]==three[i%10]:
            three_score+=1
    
    highest=max(one_score,two_score,three_score)
    if highest==one_score:
        answer.append(1)
    if highest==two_score:
        answer.append(2)
    if highest==three_score:
        answer.append(3)
    
    return answer