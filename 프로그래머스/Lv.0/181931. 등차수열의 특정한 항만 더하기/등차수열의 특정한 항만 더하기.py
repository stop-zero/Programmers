def solution(a, d, included):
    return sum((a + i * d) for i, include in enumerate(included) if include)
