A = list(map(int, input("Enter list elements: ").split()))
B = []
for x in A:
    x=x*x*x
    B.append(x)
print(B)
