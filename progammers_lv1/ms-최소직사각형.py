def solution(sizes):
    answer = 0
    # 제일 큰 수가 있는 쪽을 맞춰놓고 그 자리에 더 큰값들이 들어가게 다 정렬을 하고 그 반대쪽에서 최댓값을 찾으면 됨.
    # 더 큰 쪽에서 최대값, 더 작은 쪽에서 최대값
    greater_max=0
    lesser_max=0
    for k,v in sizes:
        if k>v:
            if k>greater_max:
                greater_max=k
            if v>lesser_max:
                lesser_max=v
        else:
            if v>greater_max:
                greater_max=v
            if k>lesser_max:
                lesser_max=k
    
    answer=greater_max * lesser_max
    return answer