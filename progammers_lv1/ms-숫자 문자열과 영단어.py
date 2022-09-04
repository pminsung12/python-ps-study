def solution(sentence):
    answer = ""
    ss=""
    for s in sentence:
        #print(f"answer: {answer}")
        #print(f"ss: {ss}")
        if ss=='zero':
            answer+='0'
            ss=""
        elif ss=='one':
            answer+='1'
            ss=""
        elif ss=='two':
            answer+='2'
            ss=""
        elif ss=='three':
            answer+='3'
            ss=""
        elif ss=='four':
            answer+='4'
            ss=""
        elif ss=='five':
            answer+='5'
            ss=""
        elif ss=='six':
            answer+='6'
            ss=""
        elif ss=='seven':
            answer+='7'
            ss=""
        elif ss=='eight':
            answer+='8'
            ss=""
        elif ss=='nine':
            answer+='9'
            ss=""
        
        
        if s.isdigit():
            answer+=s
        else:
            ss+=s
    if ss=='zero':
        answer+='0'
        ss=""
    elif ss=='one':
        answer+='1'
        ss=""
    elif ss=='two':
        answer+='2'
        ss=""
    elif ss=='three':
        answer+='3'
        ss=""
    elif ss=='four':
        answer+='4'
        ss=""
    elif ss=='five':
        answer+='5'
        ss=""
    elif ss=='six':
        answer+='6'
        ss=""
    elif ss=='seven':
        answer+='7'
        ss=""
    elif ss=='eight':
        answer+='8'
        ss=""
    elif ss=='nine':
        answer+='9'
        ss=""        
    #print(f"answer: {answer}")    
    res=int(answer)
    return res