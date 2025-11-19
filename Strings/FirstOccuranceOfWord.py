A="aabababaa"
B="ba"
n=len(A)
m=len(B)
for i in range(n-m+1):
    match=True
    for j in range(m):
        if A[i+j]!=B[j]:
            match=False
            break
    if match:
            print(i)
            break
else:
    print(0)