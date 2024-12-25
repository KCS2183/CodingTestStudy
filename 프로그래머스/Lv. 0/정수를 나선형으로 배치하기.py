# 프로그래머스 문제

# 문제 제목: 정수를 나선형으로 배치하기
# 난이도: Lv. 0

# v1 - 2024.12.21
def solution(n):
    num = 1

    direction = 'right' # 진행 방향 플래그

    top = 0
    bottom = n-1
    left = 0
    right = n-1

    arr = [[0 for _ in range(n)] for _ in range(n)]

    while(num <= n*n):
        # 파이썬은 switch문이 존재하지 않는다
        if direction == 'right':
            for j in range(left, right+1):
                arr[top][j] = num
                num += 1
            top += 1
            direction = 'down'

        elif direction == 'down':
            for i in range(top, bottom+1):
                arr[i][right] = num
                num += 1
            right -= 1
            direction = 'left'
        
        elif direction == 'left':
            for j in range(right, left-1, -1):
                arr[bottom][j] = num
                num += 1
            bottom -= 1
            direction = 'up'

        elif direction == 'up':
            for i in range(bottom, top-1, -1):
                arr[i][left] = num
                num += 1
            left += 1
            direction = 'right'

    answer = arr
    return answer