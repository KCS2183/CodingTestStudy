# 백준 문제

# 문제 번호: 7785
# 문제 제목: 회사에 있는 사람
# 난이도(solved.ac 기준): Silver 5
# 시간 제한: 1 초
# 메모리 제한: 256 MB

# v1 - 2025.01.15(시간: 188 ms, 메모리: 48.37 MB)
from sys import stdin
n = int(stdin.readline())
employees = {}

for _ in range(n):
    name, log = stdin.readline().rstrip().split()
    if log == 'enter':
        if name not in employees:
            employees[name] = log
    else:
        if name in employees:
            del employees[name]

print(*sorted(employees, reverse=True), sep='\n')


# v2
from sys import stdin
n = int(stdin.readline())
employees = set()

for _ in range(n):
    name, log = stdin.readline().rstrip().split()
    if log == 'enter':
        if name not in employees:
            employees.add(name)
    else:
        if name in employees:
            employees.remove(name)

print(*sorted(employees, reverse=True), sep='\n')


# v3
from sys import stdin

n = int(stdin.readline())
employees = set()

for _ in range(n):
    name, log = stdin.readline().rstrip().split()
    if log == 'enter':
        employees.add(name)
    else:
        employees.discard(name)  # discard는 요소가 없어도 오류가 발생하지 않음

print(*sorted(employees, reverse=True), sep='\n')