# 백준 문제

# 문제 번호: 2798
# 문제 제목: 블랙잭
# 난이도(solved.ac 기준): Bronze 2

# v1 - 2024.12.25
n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0

for i in range(n-2):
    sum = 0
    for j in range(i+1, n-1):
        for k in range(j+1, n):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= m and answer < sum:
                answer = sum

# print(answer)


# v2 - 2024.12.25
import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))

answer = 0
    
for comb in itertools.combinations(cards, 3):
    current_sum = sum(comb)
    if current_sum <= m and current_sum > answer:
        answer = current_sum

print(answer)