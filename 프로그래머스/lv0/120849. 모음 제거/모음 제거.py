def solution(my_string):
    str = ['a','e','i','o','u']
    answer = my_string
    for i in str:
        answer = answer.replace(i, '')   
    return answer