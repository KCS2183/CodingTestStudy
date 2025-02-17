# 백준 문제

# 문제 번호: 10773
# 문제 제목: 제로
# 난이도(solved.ac 기준): Silver 4
# 시간 제한: 1 초
# 메모리 제한: 256 MB

# v1 - 2025.02.11(시간: 72 ms, 메모리: 32.41 MB)
from sys import stdin

k = int(stdin.readline())
stack = []

for _ in range(k):
    num = int(stdin.readline())

    if num > 0:
        stack.append(num)
    else:
        stack.pop()

print(sum(stack))