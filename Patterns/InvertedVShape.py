n = int(input("Enter no. of rows "))

for i in range(n, 0, -1):
    print("*", end="")
    for j in range(i-1):
        print("_", end="")
    print("*")
