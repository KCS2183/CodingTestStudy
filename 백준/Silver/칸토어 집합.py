# 백준 문제

# 문제 번호: 4779
# 문제 제목: 칸토어 집합
# 난이도(solved.ac 기준): Silver 3
# 시간 제한: 1 초
# 메모리 제한: 128 MB

# v1 - 2025.02.11(시간: 68 ms, 메모리: 38.41 MB)
from sys import stdin

def cantor(i, n): # i는 시작 인덱스, n은 요소의 개수
    if n == 1:
        return
    else:
        arr[i + n//3: i + n//3 *2] = ' ' * (n//3)
        cantor(i, n//3)
        cantor(i + n//3 *2, n//3)

while True:
    try:
        num = int(stdin.readline())
        arr = ['-'] * (3**num)
        cantor(0, 3**num)
        print(''.join(arr))
    except:
        break