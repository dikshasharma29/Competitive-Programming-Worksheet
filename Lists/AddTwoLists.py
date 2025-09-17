A1 = list(map(int, input("Enter first list: ").split()))
A2 = list(map(int, input("Enter second list: ").split()))

result = []
for i in range(len(A1)):
    result.append(A1[i] + A2[i])

print(result)
