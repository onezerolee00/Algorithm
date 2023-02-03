for _ in range(int(input())):
    # k: 층 수  n: 호 수
    k = int(input())
    n = int(input())

    residents = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            residents[j] += residents[j-1]

    print(residents[-1])
