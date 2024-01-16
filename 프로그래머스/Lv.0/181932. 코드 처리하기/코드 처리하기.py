def solution(code):
    mode = True
    ret = ''
    for idx, val in enumerate(code):
        if mode:
            if val != '1' and idx % 2 == 0:
                ret = ret + val
            elif val == '1':
                mode = False         
        else:
            if val != '1' and idx % 2 != 0:
                ret = ret + val
            elif val == '1':
                mode = True
    if len(ret) == 0:
        return 'EMPTY'            
    return ret