# 백준 문제

# 문제 번호: 14914
# 문제 제목: 사과와 바나나 나눠주기
# 난이도(solved.ac 기준): Bronze 2

# v1 - 2024.12.25
a, b = map(int, input().split())

for i in range(1, 1001):
    if a%i == 0 and b%i == 0:
        print(i, a//i, b//i)


# v2 - 2024.12.25
a, b = map(int, input().split())

for i in range(1, min(a, b)+1):
    if a%i == 0 and b%i == 0:
        print(i, a//i, b//i)