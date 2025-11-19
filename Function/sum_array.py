N = int(input().strip())
arr = list(map(int, input().split()))

total = 0
i = 0
while i < N:
    total += arr[i]
    i += 1

print(total)
