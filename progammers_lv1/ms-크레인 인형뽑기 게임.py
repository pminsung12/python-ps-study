def solution(board, moves):
    answer = 0
    stk=[] # 바구니
    pick=0 #꺼낸 인형
    for m in moves:# 집게 이동
        for i in range(len(board)): # 가로 줄로 for문
            if board[i][m-1] == 0:
                continue
            pick=board[i][m-1] 
            board[i][m-1]=0 # 꺼냈으면 0
            break
        if pick==0:# 그 줄이 다 비었을 때
            continue
        if stk:
            if stk[-1]==pick: # 마지막이 똑같으면
                stk.pop() # 펑
                answer+=2
            else:
                stk.append(pick)
        else:
            stk.append(pick)
        pick=0 # 못 꺼냈을 수도 있으니 항상 끝날 때마다 초기화
    return answer