from collections import defaultdict


def solution(nums):
    answer = 0
    n_dic = defaultdict(int)
    for i in nums:
        n_dic[i] += 1
    if len(n_dic.keys()) > len(nums)/2:
        return len(nums)/2
    return len(n_dic.keys())
