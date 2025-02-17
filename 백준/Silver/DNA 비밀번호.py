# 백준 문제

# 문제 번호: 12891
# 문제 제목: DNA 비밀번호
# 난이도(solved.ac 기준): Silver 2
# 시간 제한: 2 초
# 메모리 제한: 512 MB

# v1 - 2025.02.12(시간: 420 ms, 메모리: 33.54 MB)
from sys import stdin

s, p = map(int, stdin.readline().split())
dna_str = stdin.readline().rstrip()
min_a, min_c, min_g, min_t = map(int, stdin.readline().split())

answer = 0

a_cnt = dna_str[0:p].count('A')
c_cnt = dna_str[0:p].count('C')
g_cnt = dna_str[0:p].count('G')
t_cnt = dna_str[0:p].count('T')

if a_cnt >= min_a and c_cnt >= min_c and g_cnt >= min_g and t_cnt >= min_t:
        answer += 1

for i in range(s-p):
    # 부분 문자열에서 나가는 문자
    if dna_str[i] == 'A':
        a_cnt -= 1
    elif dna_str[i] == 'C':
        c_cnt -= 1
    elif dna_str[i] == 'G':
        g_cnt -= 1
    elif dna_str[i] == 'T':
        t_cnt -= 1

    # 부분 문자열에 들어오는 문자
    if dna_str[i+p] == 'A':
        a_cnt += 1
    elif dna_str[i+p] == 'C':
        c_cnt += 1
    elif dna_str[i+p] == 'G':
        g_cnt += 1
    elif dna_str[i+p] == 'T':
        t_cnt += 1
    
    if a_cnt >= min_a and c_cnt >= min_c and g_cnt >= min_g and t_cnt >= min_t:
        answer += 1

print(answer)