# 백준 문제

# 문제 번호: 1764
# 문제 제목: 듣보잡
# 난이도(solved.ac 기준): Silver 4
# 시간 제한: 2 초
# 메모리 제한: 256 MB

# v1 - 2025.01.15(시간 초과)
n, m = map(int, input().split())

name_arr = []
count_arr = []

for _ in range(n):
    name_arr.append(input())

for _ in range(m):
    name = input()
    if name in name_arr:
        count_arr.append(name)

count_arr.sort()

print(len(count_arr))
print(*count_arr, sep='\n')


# v2 - 2025.01.15(시간 초과)
from sys import stdin
n, m = map(int, stdin.readline().split())

name_arr = []
count_arr = []

for _ in range(n):
    name_arr.append(stdin.readline().strip())

for _ in range(m):
    name = stdin.readline().strip()
    if name in name_arr:
        count_arr.append(name)

count_arr.sort()

print(len(count_arr))
print(*count_arr, sep='\n')


# v3 - 2025.01.15(시간: 80 ms, 메모리: 37.40 MB)
from sys import stdin
n, m = map(int, stdin.readline().split())

name_dict = {}
count_dict = {}

for _ in range(n):
    name_dict[stdin.readline().strip()] = 0

for _ in range(m):
    name = stdin.readline().strip()
    if name in name_dict:
        count_dict[name] = 0

print(len(count_dict))
print(*sorted(count_dict), sep='\n')


# v4
from sys import stdin
n, m = map(int, stdin.readline().split())

name_set = set()
count_set = set()

for _ in range(n):
    name_set.add(stdin.readline().strip())

for _ in range(m):
    name = stdin.readline().strip()
    if name in name_set:
        count_set.add(name)

print(len(count_set))
print(*sorted(count_set), sep='\n')


# v5
from sys import stdin

n, m = map(int, stdin.readline().split())

name_set = {stdin.readline().strip() for _ in range(n)}
count_set = {stdin.readline().strip() for _ in range(m)} & name_set # &는 교집합을 의미

print(len(count_set))
print(*sorted(count_set), sep='\n')