# 백준 문제

# 문제 번호: 32941
# 문제 제목: 왜 맘대로 예약하냐고
# 난이도(solved.ac 기준): Bronze 4

# v1 - 2024.12.28
t, x = map(int, input().split()) # t는 입력은 받지만 쓰이지 않음
n = int(input())
condition = 'YES'

for _ in range(n):
    k = int(input()) # k는 입력은 받지만 쓰이지 않음
    a = list(map(int, input().split()))

    if x not in a:
        condition = 'NO'
        break

print(condition)


# v2 - 2024.12.30
t, x = map(int, input().split()) # t 안 쓰임

for _ in range(int(input())):
    input() # v1에서 k에 값 저장을 저장하지 않는 걸로 수정
    
    if x not in map(int, input().split()): # 배열에 저장하지 않고 바로 조건으로 사용
        print('NO')
        exit() # condition 변수를 제거하여 프로그램 종료로 수정

print('YES')