def solution(a, b, c, d):
    counts = {a, b, c, d}
    result = [a, b, c, d]

    # Case 1: 모든 숫자가 같을 때
    if len(counts) == 1:
        return 1111 * a
    # Case 2: 두 숫자가 같을 때
    elif len(counts) == 2:
        if result.count(a) == 2:
            return sum(counts) * abs(list(counts)[0] - list(counts)[1])
        else:
            # Case 2-2: 두 숫자가 다를 때
            for i in result:
                if result.count(i) == 1:
                    b = i
                else:
                    c = i
            return (10 * c + b) ** 2
    # Case 3: 세 숫자가 모두 다를 때
    elif len(counts) == 3:
        # 차이가 같은 두 숫자를 선택하고 곱셈
        for i in result:
            if result.count(i) == 2:
                c = i
        counts.remove(c)
        return list(counts)[0] * list(counts)[1]
    # Case 4: 네 숫자가 모두 다를 때, 가장 작은 값 반환
    else:
        return min(result)
