def solution(myString, pat):
    idx = myString.rfind(pat)
    if idx != -1:
        return myString[:idx + len(pat)]