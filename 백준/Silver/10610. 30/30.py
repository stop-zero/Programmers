def find_largest_multiple(N):
    digits = [int(d) for d in str(N)]
    if 0 not in digits or sum(digits) % 3 != 0:
        return -1
    
    digits.sort(reverse=True)
    largest_multiple = int(''.join(map(str, digits)))
    if largest_multiple % 30 == 0:
        return largest_multiple
    else:
        return -1

N = int(input())

result = find_largest_multiple(N)
print(result)
