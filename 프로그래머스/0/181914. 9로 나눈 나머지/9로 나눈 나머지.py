def solution(number):
    digit_sum = sum(int(digit) for digit in str(number))
    remainder = digit_sum % 9
    return remainder
