def check_number(num):
    if num % 3 == 0 and num % 10 == 4:
        return True
    return False

# Example usage
number = int(input("Enter a number: "))
if check_number(number):
    print(f"{number} is divisible by 3 and ends with 4.")
else:
    print(f"{number} does not meet the criteria.")
