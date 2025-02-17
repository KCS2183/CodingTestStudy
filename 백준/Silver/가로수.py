# 백준 문제

# 문제 번호: 2485
# 문제 제목: 가로수
# 난이도(solved.ac 기준): Silver 4
# 시간 제한: 1 초
# 메모리 제한: 128 MB

# v1 - 2025.01.22(시간 초과)
from sys import stdin

def gcd_(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(stdin.readline())
a, b, gcd, count = 0, 0, 0, 0

for i in range(n-1):
    if i > 0:
        a = b
        b = int(stdin.readline())

        gcd = gcd_(gcd, b-a)
    else:
        a = int(stdin.readline())
        c = a # 시작 위치 저장
        b = int(stdin.readline())

        gcd = b-a

for _ in range(c, b+1, gcd):
    count += 1

print(count-n)


# v2 - 2025.01.22(시간 초과)
from sys import stdin

def gcd_(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(stdin.readline())
a, b, gcd, count = 0, 0, 0, 0
arr = [0] * n

for i in range(n):
    arr[i] = int(stdin.readline())

gcd = arr[1] - arr[0]

for i in range(1, n-1):
    c = gcd_(gcd, arr[i+1] - arr[i])
    if gcd == c:
        break
    else:
        gcd = c

for _ in range(arr[0], arr[n-1]+1, gcd):
    count += 1

print(count-n)


# v3 - 2025.01.22(시간: 120 ms, 메모리: 39.94 MB)
from sys import stdin

def gcd_(a, b):
    while b != 0:
        a, b = b, a%b
    return a

n = int(stdin.readline())
arr = [int(stdin.readline()) for _ in range(n)]

gaps = []
for i in range(1, n):
    gaps.append(arr[i] - arr[i-1])

gcd = gaps[0]
for gap in gaps[1:]:
    gcd = gcd_(gcd, gap)

count = 0
for gap in gaps:
    count += (gap//gcd) - 1

print(count)