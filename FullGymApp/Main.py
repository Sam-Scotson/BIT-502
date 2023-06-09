import PySimpleGUI as sg
import Membership_form
import Search_form
import Fitness_form
import Help_screen
layout = [
    [sg.Text("Welcome to the Gym Membership Application!")],
    [sg.Button("New Membership"), sg.Button("Search Memberships"), sg.Button("Class Enrollment"), sg.Button("Help"), sg.Button("Exit")]
]

window = sg.Window("Gym Membership Application", layout)

# Event loop for the main screen window
while True:
    event, _ = window.read()
    if event == "New Membership":
        window.close()
        Membership_form.new_membership_form()
    elif event == "Search Memberships":
        window.close()
        Search_form.search_members_form()
    elif event == "Class Enrollment":
        window.close()
        Fitness_form.fitness_form()
    elif event == "Help":
        window.close()
        Help_screen.help_screen()
    elif event == "Exit" or event == sg.WIN_CLOSED:
        break

window.close()