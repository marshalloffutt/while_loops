# 7-5

prompt = "How old are you?"
prompt += " Please number of years. Enter 'quit' when you are done."

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)
    if age < 3:
        print("This one's on the house!")
    elif age < 13:
        print("That'll be $10, please.")
    else:
        print("That'll be a whopping $15!! Should have done the matinee, chump.")
