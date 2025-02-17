# 백준 문제

# 문제 번호: 3273
# 문제 제목: 두 수의 합
# 난이도(solved.ac 기준): Silver 3
# 시간 제한: 1 초
# 메모리 제한: 128 MB

# v1 - 2025.02.04(시간 초과)
from sys import stdin
import itertools

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

for comb in itertools.combinations(numbers, 2):
    if sum(comb) == x:
        count += 1

print(count)


# v2 - 2025.02.04(시간 초과)
from sys import stdin

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

for i in range(n-1):
    for j in range(i+1, n):
        if numbers[i] + numbers[j] == x:
            count += 1

print(count)


# v3 - 2025.02.04(시간 초과)
from sys import stdin

n = int(stdin.readline())
numbers = list(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

for i in range(n):
    if x - numbers[i] in numbers:
        count += 1

print(count//2) # 중복 제거를 위해 2로 나누기


# v4 - 2025.02.04(시간: 68 ms, 메모리: 45.92 MB)
'''
python에서 list와 set의 in 연산 시간 복잡도 차이는 자료구조의 내부 구현 방식에 기인한다.

list는 순차적 탐색 방식으로 구현되어 있다. 즉, list에서 특정 값이 있는지 찾을 때, Python에서는 처음부터 끝까지 하나씩 확인해야 한다.
만약 배열의 길이가 n이라면, 최악의 경우 마지막 원소까지 확인해야 하므로, list의 in 연산은 O(n) 시간이 걸린다.

set은 해시 테이블 구조로 구현되어 있다. set에서 in 연산을 수행할 때, 값은 먼저 해시 함수를 사용하여 해시값을 계산한 후,
해당 해시값에 맞는 버킷에서 값을 찾는다. 이 과정은 상수 시간에 이루어지므로, 평균적으로 O(1) 시간이 걸린다.
'''
from sys import stdin

n = int(stdin.readline())
numbers = set(map(int, stdin.readline().split()))
x = int(stdin.readline())
count = 0

for num in numbers:
    if x - num in numbers:
        count += 1

print(count//2)