def solution(arr):
    answer = []
    list=[]
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i]==2:
                list.append(i)
    return arr[list[0]:list[-1]+1]