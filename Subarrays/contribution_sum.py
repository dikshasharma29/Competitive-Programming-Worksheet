N = int(input().strip())
arr = list(map(int, input().split()))

total = 0
i = 0

while i < N:
    left = i + 1
    right = N - i
    total += arr[i] * left * right
    i += 1

print(total)
