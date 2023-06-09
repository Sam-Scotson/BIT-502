import PySimpleGUI as sg

def help_screen():
    layout = [
        [sg.Text("Gym Membership Application Help", font=("Arial", 16))],
        [sg.Text("Welcome to the Gym Membership Application!")],
        [sg.Text("This application allows you to perform various tasks related to gym membership management.")],
        [sg.Text("")],
        [sg.Text("Main Screen:")],
        [sg.Text("- Use the navigation buttons to access different forms.")],
        [sg.Text("")],
        [sg.Text("Membership Form:")],
        [sg.Text("- Fill in the personal information fields.")],
        [sg.Text("- Select the membership type, duration, and payment frequency.")],
        [sg.Text("- Choose any additional extras.")],
        [sg.Text("- Click 'Calculate' to display the total payment.")],
        [sg.Text("- Click 'Submit' to save the membership information.")],
        [sg.Text("")],
        [sg.Text("Search Form:")],
        [sg.Text("- Enter the member's last name.")],
        [sg.Text("- Click 'Search' to find members with a matching last name.")],
        [sg.Text("")],
        [sg.Text("Fitness Form:")],
        [sg.Text("- Select the fitness class from the dropdown.")],
        [sg.Text("- Enter the member's last name.")],
        [sg.Text("- Click 'Enroll' to enroll the member in the selected class.")],
        [sg.Text("")],
        [sg.Text("Help Screen:")],
        [sg.Text("- Displays information on how to use the application.")],
        [sg.Text("- Contains instructions and guidelines.")],
        [sg.Text("")],
        [sg.Button("Close")]
    ]

    window = sg.Window("Help", layout)

    # Event loop for the help screen window
    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            window.close()
            break