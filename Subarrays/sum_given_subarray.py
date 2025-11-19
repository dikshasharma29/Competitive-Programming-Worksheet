N = int(input().strip())
arr = list(map(int, input().split()))
L, R = map(int, input().split())  

total = 0
i = L - 1
while i <= R - 1:
    total += arr[i]
    i += 1

print(total)
