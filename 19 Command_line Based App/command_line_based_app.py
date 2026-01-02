from datetime import datetime

todo_items = []

while True:
    todo = input("Enter your to-do items for today. Type 'done' to save and exit: ")
    if todo == "done":
        break
    todo_items.append(todo)


day = datetime.now().strftime("%Y-%m-%d")
filename = f"{day}.txt"

content = "\n".join(todo_items)

with open(filename, "w") as file:
    file.write(content)

print(f"Your to-do list is saved successfully !!")