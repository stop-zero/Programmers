score_sum, score_diff = map(int, input().split())

score_a = (score_sum + score_diff) // 2
score_b = (score_sum - score_diff) // 2

if score_a >= 0 and score_b >= 0 and (score_a + score_b) == score_sum and (score_a - score_b) == score_diff:
    print(max(score_a, score_b), min(score_a, score_b))
else:
    print(-1)
