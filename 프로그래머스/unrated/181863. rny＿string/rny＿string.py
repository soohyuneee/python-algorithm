def solution(rny_string):
    answer = ''
    for i in rny_string:
        temp = i.replace("m", "rn")
        answer += temp
    return answer