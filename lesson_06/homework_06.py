user_input = input("Write your text: ")

print(True if len(set(user_input)) > 10 else False)
