N = int(input().strip())
if N <= 0:
    print(0)
elif N == 1 or N == 2:
    print(1)
else:
    a, b = 1, 1
    i = 3
    while i <= N:
        c = a + b
        a, b = b, c
        i += 1
    print(b)
  
