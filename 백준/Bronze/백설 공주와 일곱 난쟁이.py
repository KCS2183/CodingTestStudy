# 백준 문제

# 문제 번호: 3040
# 문제 제목: 백설 공주와 일곱 난쟁이
# 난이도(solved.ac 기준): Bronze 2

# v1 - 2024.12.30
import itertools

data = []
answer = []

for i in range(9):
    data.append(int(input()))

for comb in itertools.combinations(data, 7):
    if sum(comb) == 100:
        answer.extend(comb)
        break

for i in range(7):
    print(answer[i])


# v2 - 2024.12.30
import itertools

data = []

for i in range(9):
    data.append(int(input()))

for comb in itertools.combinations(data, 7):
    if sum(comb) == 100:
        for num in comb: # 튜플도 순회할 수 있음
            print(num)
        break


# v3 - 2025.01.01
import itertools

data = []

for i in range(9):
    data.append(int(input()))

for comb in itertools.combinations(data, 7):
    if sum(comb) == 100:
        for num in comb: # 튜플도 순회할 수 있음
            print(num)
        exit() # break 대신 바로 종료


# v4 - 2025.01.14
data = []

for i in range(9):
    data.append(int(input()))

target_sum = sum(data) - 100

for i in range(9):
    for j in range(i+1, 9):
        if data[i] + data[j] == target_sum:
            del data[j] # 더 뒤에 있는 인덱스부터 삭제
            del data[i]

            for k in range(7):
                print(data[k])
            exit()


# v5 - 2025.01.15
data = []

for i in range(9):
    data.append(int(input()))

target_sum = sum(data) - 100

for i in range(9):
    for j in range(i+1, 9):
        if data[i] + data[j] == target_sum:
            del data[j] # 더 뒤에 있는 인덱스부터 삭제
            del data[i]

            print(*data, sep='\n') # 반복문 대신 리스트 언패킹 사용
            exit()