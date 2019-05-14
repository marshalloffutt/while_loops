# 7-8, 7-9

# Make a list of sandwich_orders, and fill it with sandwiches.
# Then make an empty list of finished_sandwiches.
sandwich_orders = ['pastrami', 'tuna melt', 'french dip', 'pastrami', 'turkey swiss', 'ham and cheese', 'pastrami']
finished_sandwiches = []

print("Oh no! We've run out of pastrami!")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Iterate through the sandwich_orders, and print a message for each order
# move each sandwich into the finished_sandwiches list
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print("Making " + current_sandwich + " now.")
    finished_sandwiches.append(current_sandwich)

# Print a message listing each sandwich that was made
for sandwich in finished_sandwiches:
    print("Today we made a " + sandwich + " sandwich.")
