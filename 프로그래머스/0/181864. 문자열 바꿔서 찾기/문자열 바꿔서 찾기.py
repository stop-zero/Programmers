def solution(myString, pat):
    transformed = myString.translate(str.maketrans('AB', 'BA'))
    
    if pat in transformed:
        return 1
    else:
        return 0
