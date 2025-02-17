# 백준 문제

# 문제 번호: 1934
# 문제 제목: 최소공배수
# 난이도(solved.ac 기준): Bronze 1
# 시간 제한: 1 초
# 메모리 제한: 128 MB

# v1 - 2025.01.22(시간: 36 ms, 메모리: 31.78 MB)
from sys import stdin
t = int(stdin.readline())
answer = []

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    c = a*b

    # 유클리드 호제법
    while b != 0:
        a, b = b, a%b
    
    answer.append(int(c/a))

print(*answer, sep='\n') # 반복문 순회가 다 끝나면 출력


# v2 - 2025.01.22(시간: 36 ms, 메모리: 31.65 MB)
from sys import stdin
t = int(stdin.readline())

for _ in range(t):
    a, b = map(int, stdin.readline().split())
    aa, bb = a, b

    # 유클리드 호제법
    while bb != 0:
        aa, bb = bb, aa%bb

    print(a*b//aa) # 반복문 순회 도중 출력