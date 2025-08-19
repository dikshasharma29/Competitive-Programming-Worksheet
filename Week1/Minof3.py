A = int(input("Enter number A: "))
B = int(input("Enter number B: "))
C = int(input("Enter number C: "))

minimum = A
if B < minimum:
    minimum = B
if C < minimum:
    minimum = C

print("Minimum is:", minimum)
