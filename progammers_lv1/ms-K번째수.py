def solution(array, commands):
    answer = []
    new_list = []
    front = 0
    end = 0
    idx = 0
    for case in commands:
        front, end, idx = case[0], case[1], case[2]-1
        new_list = array[front-1:end]
        new_list.sort()
        answer.append(new_list[idx])

    return answer
