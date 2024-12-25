# 프로그래머스 문제

# 문제 제목: 삼총사
# 난이도: Lv. 1

# v1 - 2024.12.21
def solution(number):
    count = 0

    for i, value1 in enumerate(number):
        for j, value2 in enumerate(number):
            for k, value3 in enumerate(number):
                if value1 + value2 + value3 == 0 and i < j and j < k:
                    count += 1

    answer = count
    return answer


# v2 - 2024.12.25
def solution(number):
    answer = 0
    length = len(number)
    
    for i in range(length-2):
        for j in range(i+1, length-1):
            for k in range(j+1, length):
                if number[i] + number[j] + number[k] == 0:
                    answer += 1
    
    return answer