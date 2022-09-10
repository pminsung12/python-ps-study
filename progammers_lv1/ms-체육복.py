# for문 돌면서 remove 사용하면 몇 개가 순회에서 빠지는 문제가 생길 수 있어 리스트 하나 더 사용하기
def solution(n, lost, reserve):
    answer = n
    found=0
    lost.sort()
    reserve.sort()
    new_lost=[]
    for i in lost:#중복제거
        if i in reserve:
            reserve.remove(i)
        else:
            new_lost.append(i)
    
    lost=new_lost # 중복 제거한 도난리스트
    
    for i in lost:
        for j in reserve:
            if j==i-1 or j==i+1:
                found=1
                reserve.remove(j)
                break
            
        if not found:
            answer-=1
        found=0
    return answer

