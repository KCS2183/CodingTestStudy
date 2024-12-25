# 프로그래머스 문제

# 문제 제목: 없는 숫자 더하기
# 난이도: Lv. 1

# v1 - 2024.12.21
def solution(numbers):
    sum = 0

    for i in range(0, 10):
        if i not in numbers:
            sum += i

    answer = sum
    return answer


# v2 - 2024.12.23
def solution(numbers):
    return 45 - sum(numbers)