# 백준 문제

# 문제 번호: 1157
# 문제 제목: 단어 공부
# 난이도(solved.ac 기준): Bronze 1
# 시간 제한: 2 초
# 메모리 제한: 128 MB

# v1 - 2025.02.12(가장 많이 사용된 알파벳이 여러 개 존재하는 경우 '?'를 출력해야 한다는 조건을 놓침)
from collections import Counter
from sys import stdin

word = stdin.readline().strip()
counter = Counter(word.upper())

'''
Counter.most_common(n) 함수는 가장 자주 등장한 항목들을 리스트로 반환하는데 리스트의 각 항목은 (값, 빈도) 형태로 저장됨.
또한 n을 통해 반환할 개수를 지정할 수 있음.
'''
most_letter, count = counter.most_common(1)[0]
print(most_letter)


# v2 - 2025.02.12(시간: 124 ms, 메모리: 34.56 MB)
from collections import Counter
from sys import stdin

counter = Counter(stdin.readline().strip().upper())
max_count = max(counter.values())
most_letter = [letter for letter, count in counter.items() if count == max_count]

if len(most_letter) > 1:
    print('?')
else:
    print(most_letter[0])