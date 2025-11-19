A="aabbcc"
B=98
ch=chr(B)
found=False
for i in range(len(A)):
    if A[i]==ch:
        print(i)
        found=True
        break
if not found:
        print(-1)
 