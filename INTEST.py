N, K = map(int, input().split())
count = 0
while N > 0:
    a = int(input())
    if (a % K == 0):
        count += 1
    else:
        0
    N = N - 1
print(count)   