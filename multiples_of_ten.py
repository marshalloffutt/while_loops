# 7-3

# Ask user for a number
number = input("Tell me a number, and I'll tell you if it is a multiple of ten. ")

number = int(number)

if number % 10 == 0:
    print("\nYes! The number " + str(number) + " is a multiple of 10.")
else:
    print("\nNo. The number " + str(number) + " is not a multiple of 10.")