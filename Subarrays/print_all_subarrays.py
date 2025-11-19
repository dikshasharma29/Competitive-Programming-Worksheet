N = int(input().strip())
arr = list(map(int, input().split()))

i = 0
while i < N:
    j = i
    while j < N:
        k = i
        while k <= j:
            print(arr[k], end=" ")
            k += 1
        print()
        j += 1
    i += 1
