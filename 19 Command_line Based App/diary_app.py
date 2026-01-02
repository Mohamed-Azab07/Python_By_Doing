from datetime import datetime


daily_dairy = []

while True:
    dairy = input("Enter your notes for today. Type 'exit' to save and exit: \n-> ")
    if dairy == "exit":
        print("Goodbye!")
        break

    daily_dairy.append(dairy)



today = datetime.now().strftime("%A")

filename = f"{today}.txt"

content = "\n".join(daily_dairy)

with open(filename, "w") as file:
    file.write(content)