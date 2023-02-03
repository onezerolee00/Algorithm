import sys
input = sys.stdin.readline

# 출력: 필요한 동전 개수의 최솟값
# n: 동전의 종류  k: 가치의 합
n, k = map(int, input().split())

answer = 0
coins = []
for _ in range(n):
    coins.append(int(input()))

coins.reverse()

for coin in coins:
    answer += k // coin
    k %= coin

print(answer)