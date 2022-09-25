import math


def solution(n):
    isPrime = 1
    prime_lst = []

    for j in range(2, n+1):
        for i in range(2, int(math.sqrt(j)) + 1):
            if j % i == 0:
                isPrime = 0
                break
        if isPrime == 0:
            isPrime = 1
            continue
        prime_lst.append(j)  # 소수임

    return len(prime_lst)
