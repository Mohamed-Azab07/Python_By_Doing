from datetime import datetime

dairy_notes = []

while True:
    user_input = input("Enter your notes for today. Type'exit' to save and exit: \n-> ")
    if user_input == "exit":
        print("Goodbye !")
        break
    dairy_notes.append(user_input)


now = datetime.now().strftime("%A")

file_name = f"{now}.txt"

with open(file_name, "w") as file:
    file.writelines(dairy_notes)


