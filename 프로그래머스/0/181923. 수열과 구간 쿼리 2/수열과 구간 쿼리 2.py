def solution(arr, queries):
    result = []

    for query in queries:
        s, e, k = query
        sub_array = arr[s : e + 1]
        valid_elements = [element for element in sub_array if element > k]

        if valid_elements:
            result.append(min(valid_elements))
        else:
            result.append(-1)

    return result
