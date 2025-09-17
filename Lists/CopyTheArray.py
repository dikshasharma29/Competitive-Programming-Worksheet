a = list(map(int, input("Enter list elements: ").split()))
b = int(input("Enter value of B: "))
Arr = []
for x in a:
    x=x+b
    Arr.append(x)
print("New Array:", Arr)
