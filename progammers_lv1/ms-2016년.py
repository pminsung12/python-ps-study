def solution(a, b):
    answer = ''
    days = 'THU FRI SAT SUN MON TUE WED '.split()
    dates = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum_of_dates = 0
    for i in range(a-1):
        sum_of_dates += dates[i]
    sum_of_dates += b
    answer = days[sum_of_dates % 7]
    return answer
