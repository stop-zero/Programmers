def solution(my_string, is_suffix):
    res = my_string[::-1]
    
    if res.startswith(is_suffix[::-1]):
        return 1
    else:
        return 0
