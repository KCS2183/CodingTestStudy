# 백준 문제

# 문제 번호: 11478
# 문제 제목: 서로 다른 부분 문자열의 개수
# 난이도(solved.ac 기준): Silver 3
# 시간 제한: 1 초
# 메모리 제한: 512 MB

# v1 - 2025.01.15(시간 초과)
s = input()

length = len(s)
substring = []

for i in range(length):
    for j in range(i+1, length+1):
        if s[i:j] not in substring:
            substring.append(s[i:j])

print(len(substring))


# v2 - 2025.01.15(시간: 472 ms, 메모리: 231.39 MB)
s = input()

length = len(s)
substring = {}

for i in range(length):
    for j in range(i+1, length+1):
        substring[s[i:j]] = 0 # key는 중복될 수 없는 점을 이용, value는 필요 없으므로 0을 넣었음

print(len(substring)) # key의 개수 출력


# v3
s = input()

length = len(s)
substring = set()

for i in range(length):
    for j in range(i+1, length+1):
        substring.add(s[i:j]) # key는 중복될 수 없는 점을 이용

print(len(substring)) # key의 개수 출력