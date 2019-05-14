# 7-10

# Create an empty dictionary to hold all responses
responses = {}

# Set a flag to indicate that polling is active.
polling_active = True

while polling_active:
    # Prompt users for their name, and vacation spot.
    name = input("What is your name? ")
    response = input("Where do you want to go? ")

    # Store the responses into the responses dictionary
    responses[name] = response

    # Find out if anyone else wishes to provide a response
    repeat = input("Would you like to let someone else answer? (yes / no) ")
    if repeat == 'no':
        polling_active = False
    
# Polling is complete! Let's see the results...
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(name + " would like to visit " + response + ".")