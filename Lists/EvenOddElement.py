
A = list(map(int, input("Enter list elements: ").split()))

even = 0
odd = 0

for x in A:
    if x % 2 == 0:
        even += 1
    else:
        odd += 1

print("Difference:", abs(even - odd))
