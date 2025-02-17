# 백준 문제

# 문제 번호: 13241
# 문제 제목: 최소공배수
# 난이도(solved.ac 기준): Silver 5
# 시간 제한: 2 초
# 메모리 제한: 512 MB

# v1 - 2025.01.22(시간: 40 ms, 메모리: 31.65 MB)
from sys import stdin
a, b = map(int, stdin.readline().split())
aa, bb = a, b

# 유클리드 호제법
while bb != 0:
    aa, bb = bb, aa%bb

print(a*b//aa)