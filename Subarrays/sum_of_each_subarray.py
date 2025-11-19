N = int(input().strip())
arr = list(map(int, input().split()))

i = 0
while i < N:
    j = i
    while j < N:
        s = 0
        k = i
        while k <= j:
            s += arr[k]
            k += 1
        print(s)
        j += 1
    i += 1
