import sys
input = sys.stdin.readline
output = sys.stdout.write

n = int(input())
dp = [0, 1, 2] + ([0] * (n-2))

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

output(str(dp[n]))