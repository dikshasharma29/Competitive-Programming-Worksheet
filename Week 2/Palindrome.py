A = int(input("Enter number: "))

original = A
rev = 0

while A > 0:
    digit = A % 10
    rev = rev * 10 + digit
    A //= 10

if original == rev:
    print("Number is Palindrome")   # Palindrome
else:
    print("Not a Palindrome Number")    # Not palindrome
