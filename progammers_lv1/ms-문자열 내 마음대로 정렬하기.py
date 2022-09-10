def solution(strings, n):
    answer = []
    strings.sort()
    s = ''
    answer = sorted(strings, key=lambda x: x[n])
    # print(new_words)

    return answer


''' 다른사람풀이
lambda에 튜플을 넣으면 첫 번째 원소로 오름차순 정렬하고, 첫 번째 원소가 같은 경우
두 번째 원소로 오름차순 정렬한다.
def solution(strings, n):
    return sorted(strings, key=lambda x:(x[n],x))
'''
