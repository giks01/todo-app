FILEPATH = "todos.txt"

def get_todos(filepath = FILEPATH):
    """ read a text file and return the list of todo items """

    with open(filepath, "r") as file_local:
        todos_local = file_local.readlines()
        return todos_local

def write_todos(todos_args, filepath = FILEPATH):
    """ write the todo items list in the text file """
    with open("todos.txt", "w") as file:
        file.writelines(todos_args)
