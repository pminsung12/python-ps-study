def solution(arr):
    answer = []
    prev=-1
    cur=-1
    for i in range(len(arr)):
        cur=arr[i]
        if cur!=prev:
            answer.append(cur)
        prev=arr[i]
            
    return answer