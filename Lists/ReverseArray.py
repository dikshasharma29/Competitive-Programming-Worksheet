n=list(map(int,input("Enter an Array:").split( )))
rev=[]
for i in range(n-1,-1,-1):
    rev.append(n[i])
print(rev)