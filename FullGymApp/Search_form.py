import PySimpleGUI as sg

def search_members_form():
    layout = [
        [sg.Text("Search Members")],
        [sg.Text("Last Name:"), sg.Input(key="-LAST_NAME-")],
        [sg.Button("Search"), sg.Button("Cancel")],
        [sg.Text("Results:")],
        [sg.Output(size=(60, 10), key="-RESULTS-")]
    ]

    window = sg.Window("Search Members", layout)

    while True:
        event, values = window.read()
        if event == "Search":
            last_name = values["-LAST_NAME-"].strip()

            if last_name:
                members = search_members(last_name)
                if members:
                    print("Found Members:")
                    for member in members:
                        print(f"- {member}")
                else:
                    print("No members found.")

        elif event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break

def search_members(last_name):
    # This is a placeholder function that returns some dummy data
    members = []
    if last_name.lower() == "smith":
        members = ["John Smith", "Jane Smith", "David Smith"]
    elif last_name.lower() == "jones":
        members = ["Michael Jones", "Sarah Jones"]
    elif last_name.lower() == "wilson":
        members = ["Emily Wilson"]
    return members