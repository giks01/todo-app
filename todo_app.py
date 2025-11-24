from functions import get_todos, write_todos
import time
now = time.strftime("%b %d, %Y  %H:%M:%S")
print("It is ", now)

while True:
    user_interaction = input("Type add, show, edit, complete or exit:")
    user_interaction = user_interaction.strip()

    if user_interaction.startswith("add"):
       todo = user_interaction[4:]

       todos = get_todos()
       todos.append(todo + '\n')

       write_todos( todos)
    elif user_interaction.startswith("show"):

        todos = get_todos()

        for i, item in enumerate(todos):
            item = item.strip('\n')
            row= f"{i+1}.{item}"
            print(row)
    elif user_interaction.startswith("edit"):
        try:
            number = int(user_interaction[5:])
            print(number)
            number = number -1

            todos = get_todos()

            new_todo = input("Enter a new todo: ") + '\n'
            todos[number] = new_todo

            write_todos(todos)
        except ValueError:
            print("Your command is not recognized.")
            continue
    elif user_interaction.startswith("complete"):
        try:
            completed = int(user_interaction[9:])

            todos = get_todos()
            index = completed - 1
            todo_to_remove = todos[index].strip('\n')

            todos.pop(completed - 1)


            write_todos(todos)
            message = f"{todo_to_remove} was removed from the todo list"
            print(message)
        except IndexError:
            print("Your choice is out of range")
            continue

    elif user_interaction.startswith("exit"):
        break
    else:
        print("Command not recognised")
print("Bye!")

