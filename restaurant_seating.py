# 7-2

# Ask the user how many people are in their dinner group
count = input("How many people will be in your dinner group? ")

count = int(count)

# If answer is greater than 8, they will have to wait for a table.
# otherwise they can be seated.
if count > 8:
    print("You will have to wait for a table.")
else:
    print("Right this way...")