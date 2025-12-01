import functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkPurple4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key= "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")
edit_label = sg.Text(key="editing")

window = sg.Window('My to-do App',
                   layout=[[clock],
                           [label],
                           [input_box, add_button],
                           [list_box, edit_button, complete_button],
                            [exit_button]],
                   font=('Helvetica', 15))
while True:
    events, values = window.read(timeout=200)
    window["clock"].update(value = time.strftime("%b %d, %Y  %H:%M:%S"))

    match events:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("You have not selected an item to edit", font=("Helvetica", 15))
        case "Complete":
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values = todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("You have not selected an item to complete", font=("Helvetica", 15))
        case "Exit":
            break

        case "todos":
            window['todo'].update(value=values['todos'][0])
        case sg.WIN_CLOSED:
            break

window.close()