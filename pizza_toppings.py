# 7-4

prompt = "\nType the pizza toppings would you like to request:"
prompt += "\nWhen you are finished, enter 'quit' to end the program. "

message = ""

while message != 'quit':
    message = input(prompt)
    print(message)