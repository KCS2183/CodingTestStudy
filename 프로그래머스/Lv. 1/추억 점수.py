# 프로그래머스 문제

# 문제 제목: 추억 점수
# 난이도: Lv. 1

# v1 - 2024.12.21
def solution(name, yearning, photo):
    dict = {}
    result = []

    for i in range(len(name)):
        dict[name[i]] = yearning[i]

    for i in photo:
        sum = 0
        for j in i:
            if j in dict.keys():
                sum += dict[j]
        result.append(sum)

    answer = result
    return answer