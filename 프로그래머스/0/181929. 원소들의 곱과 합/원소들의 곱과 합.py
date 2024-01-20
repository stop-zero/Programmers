def solution(num_list):
    res = 1
    for num in num_list:
        res *= num

    total_sum = sum(num_list)

    if res < total_sum ** 2:
        return 1
    else:
        return 0