import PySimpleGUI as sg

def fitness_form():
    class_options = [
        "Cardio, Thursday, 3pm-5pm",
        "Pilates, Friday, 9am-11am",
        "Spin, Monday, 2pm-4pm"
    ]

    layout = [
        [sg.Text("Fitness Class Enrollment")],
        [sg.Text("Select Class:"), sg.Combo(class_options, key="-CLASS-")],
        [sg.Text("Last Name:"), sg.Input(key="-LAST_NAME-")],
        [sg.Button("Enroll"), sg.Button("Cancel")]
    ]

    window = sg.Window("Fitness Form", layout)

    while True:
        event, values = window.read()
        if event == "Enroll":
            selected_class = values["-CLASS-"]
            last_name = values["-LAST_NAME-"].strip()

            if last_name:
                enroll_member(selected_class, last_name)
                sg.popup("Enrollment successful!")
            else:
                sg.popup("Please enter a valid last name.")

        elif event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break

def enroll_member(selected_class, last_name):
    print(f"Enrolling member with last name: {last_name} in class: {selected_class}")