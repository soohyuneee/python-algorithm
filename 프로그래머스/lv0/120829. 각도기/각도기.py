def solution(angle):
    if angle == 180:
        return 4
    elif 90 < angle : 
        return 3
    elif angle == 90 : 
        return 2
    else:
        return 1