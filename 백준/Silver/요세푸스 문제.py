# 백준 문제

# 문제 번호: 1158
# 문제 제목: 요세푸스 문제
# 난이도(solved.ac 기준): Silver 4
# 시간 제한: 2 초
# 메모리 제한: 256 MB

# v1 - 2025.02.04(시간: 44 ms, 메모리: 32.65 MB)
from sys import stdin

n, k = map(int, stdin.readline().split())
people = [i+1 for i in range(n)]
index = k-1
answer = []

for _ in range(n):
    answer.append(people[index])
    del people[index]

    if people:
        index = (index +k -1) % len(people) # 인덱스 변화를 고려하여 -1

print('<' + ', '.join(map(str, answer)) + '>')