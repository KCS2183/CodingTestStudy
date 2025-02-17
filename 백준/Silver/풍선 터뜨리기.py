# 백준 문제

# 문제 번호: 2346
# 문제 제목: 풍선 터뜨리기
# 난이도(solved.ac 기준): Silver 3
# 시간 제한: 2 초
# 메모리 제한: 4 MB

# v1 - 2025.01.15(시간: 36 ms, 메모리: 31.65 MB)
from sys import stdin

n = int(stdin.readline())
values = list(map(int, stdin.readline().split()))
balloon = []
current_index = 0 # 항상 1번 풍선부터 시작하므로 인덱스는 0으로 설정

for i in range(1, n+1):
    balloon.append((i, values[i-1]))

for _ in range(n):
    x, y = balloon[current_index]
    print(x, end=' ')
    del balloon[current_index]

    if not balloon:
        break
    else:
        if y < 0:
            '''
            python의 %는 A % B가 있다고 가정하면, A에다가 B를 계속 더하면서 처음으로 양수가 되었을 때 B로 나눠 나머지 값을 준다.
            다시 말해 -1 % 10이면 9가 나오게 되는데, -1 + 10 = 9, 9 % 10 = 9 이런 과정을 거쳐 값이 나오게 된다.
            따라서 이 문제에서 y가 음수이면 그냥 current_index에 y를 더해서 balloon 배열의 길이로 나누면 왼쪽으로 y만큼 가는것처럼 보이게 된다.
            '''
            current_index = (current_index +y) % len(balloon)
        else:
            current_index = (current_index +y -1) % len(balloon) # 풍선을 터뜨려서 발생한 인덱스 변화를 고려해 -1