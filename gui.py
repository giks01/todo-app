import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter to-do", key= "todo")
add_button = sg.Button("Add")

window = sg.Window('My to-do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 15))
while True:
    events, values = window.read()
    print(events)
    print(values)
    match events:
        case "Add":
            todos = functions.get_todos()
            new_todos = values['todo'] + "\n"
            todos.append(new_todos)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()