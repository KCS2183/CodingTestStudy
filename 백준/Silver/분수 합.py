# 백준 문제

# 문제 번호: 1735
# 문제 제목: 분수 합
# 난이도(solved.ac 기준): Silver 3
# 시간 제한: 2 초
# 메모리 제한: 128 MB

# v1 - 2025.01.22(시간: 32 ms, 메모리: 31.78 MB)
a, b = map(int, input().split())
c, d = map(int, input().split())

e = a*d + c*b
f = b*d

n, d = e, f

while d != 0:
    n, d = d, n%d

print(e//n, f//n)


# v2 - 2025.01.22(시간: 36 ms, 메모리: 31.65 MB)
from sys import stdin
a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())

e = a*d + c*b
f = b*d

n, d = e, f

while d != 0:
    n, d = d, n%d

print(e//n, f//n)


# v3 - 2025.01.22(시간: 32 ms, 메모리: 31.65 MB)
from sys import stdin

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

a, b = map(int, stdin.readline().split())
c, d = map(int, stdin.readline().split())

e = a*d + c*b
f = b*d
g = gcd(e, f)

print(e//g, f//g)