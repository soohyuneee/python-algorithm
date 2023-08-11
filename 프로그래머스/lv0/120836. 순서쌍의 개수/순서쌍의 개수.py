def solution(n):
    answer = 0
    num = 1
    while num <= n :
        if n % num == 0:
            answer+=1
        num += 1
    return answer