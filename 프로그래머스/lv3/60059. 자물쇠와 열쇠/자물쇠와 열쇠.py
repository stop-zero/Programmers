def solution(key, lock):
    M = len(key) 
    N = len(lock)
    # list
    key = [key] 
    
    def init(M): # 배열 0으로 초기화 생성
        res = [] # key 후보 list 생성
        for m in range(M):
            tmp = []
            for n in range(M):
                tmp.append(0)
            res.append(tmp)
        return res

    def padding(lock, N, M): # 계산을 위한 0으로 padding
        T = N + 2 * (M - 1)
        res = []
        for m in range(T):
            tmp = []
            for n in range(T):
                tmp.append(0)
            res.append(tmp)

        for i in range(N):
            for j in range(N):
                res[i + M - 1][j + M - 1] = lock[i][j]

        return res

    def check(key, lock_padding): 
        import copy
        T = len(lock_padding)
        M = len(key)
        for gap1 in range(T - M + 1): 
            for gap2 in range(T - M + 1):
                res = True
                cand_padding = copy.deepcopy(lock_padding)
                for p in range(M):
                    for q in range(M):
                        cand_padding[p + gap1][q + gap2] += key[p][q]
                check_area = []
                for p in range(M - 1, T - M + 1):
                    tmp = []
                    for q in range(M - 1, T - M + 1):
                        tmp.append(cand_padding [p][q])
                    check_area.append(tmp)

                for p in range(len(check_area)):
                    for q in range(len(check_area)):
                        if check_area[p][q] != 1:
                            res = False
                            break
                    if res == False:
                        break
                if res == True:
                    return res
        return False

    # key 후보 다 뽑기
    for i in range(3):
        new_key = init(M)
        for p in range(M):
            for q in range(M):
                new_key[q][M - 1 - p] = key[-1][p][q]
        key.append(new_key)

    # lock padding
    lock_padding = padding(lock, N, M)

    answer = False
    for i in range(4):
        cand_key = key[i]
        if check(cand_key, lock_padding) == True:
            return True

    return answer

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
res =solution(key, lock)