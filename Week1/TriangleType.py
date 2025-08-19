a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))


  
if (a > 0 and b > 0 and c > 0):
        if (a == 90 and b == 90 and c == 90):
            print("Right triangle")
        elif ( a > 90 and b > 90 and c > 90):
            print("Obtuse triangle")
        elif (a < 90 and b <90 and c < 90):
            print("Acute triangle")
else:
    print("Not a valid triangle")