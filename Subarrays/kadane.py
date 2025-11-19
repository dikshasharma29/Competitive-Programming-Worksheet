N = int(input().strip())
arr = list(map(int, input().split()))

max_sum = arr[0]
current = 0
i = 0

while i < N:
    current += arr[i]

    if current > max_sum:
        max_sum = current

    if current < 0:
        current = 0

    i += 1

print(max_sum)
