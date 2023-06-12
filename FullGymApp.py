import sqlite3
import PySimpleGUI as sg

# Connect to the SQLite database
conn = sqlite3.connect("gym_database.db")
cursor = conn.cursor()

# Function to insert new member data into the Members table
def insert_member_data(data):
    try:
        cursor.execute("""
            INSERT INTO Members (first_name, last_name, address, mobile_number, payment_frequency, extras, regular_payment)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, data)
        conn.commit()
        sg.popup("New member registered successfully!")
    except sqlite3.Error as e:
        sg.popup("Error occurred while registering the member:", str(e))

def search_members(last_name):
    # Placeholder function - Replace with your actual implementation to search for members based on last name
    members = []
    if last_name.lower() == "smith":
        members = ["John Smith", "Jane Smith", "David Smith"]
    elif last_name.lower() == "jones":
        members = ["Michael Jones", "Sarah Jones"]
    elif last_name.lower() == "wilson":
        members = ["Emily Wilson"]
    return members

def enroll_member(selected_class, last_name):
    # Placeholder function - Replace with your actual implementation to enroll a member in a fitness class
    print(f"Enrolling member with last name: {last_name} in class: {selected_class}")

def new_membership_form():
    membership_options = ["Basic: $10pw", "Regular: $15pw", "Premium: $20pw"]
    duration_options = ["3 Months", "12 Months", "24 Months"]
    extras_options = [
        "24/7 Access: $1pw",
        "Personal Trainer: $20pw",
        "Diet Consultation: $20pw",
        "Online Fitness Video: $2pw"
    ]

    layout = [
        [sg.Text("New Membership Form")],
        [sg.Text("First Name:"), sg.Input(key="-FIRST_NAME-")],
        [sg.Text("Last Name:"), sg.Input(key="-LAST_NAME-")],
        [sg.Text("Address:"), sg.Input(key="-ADDRESS-")],
        [sg.Text("Phone Number:"), sg.Input(key="-PHONE_NUMBER-")],
        [sg.Text("Membership Type:"), sg.Combo(membership_options, key="-MEMBERSHIP_TYPE-")],
        [sg.Text("Membership Duration:"), sg.Combo(duration_options, key="-DURATION-")],
        [sg.Text("Membership Extras:")],
        [sg.Column([
            [sg.Checkbox(extra, key=f"-EXTRA-{i}-")] for i, extra in enumerate(extras_options)
        ], scrollable=True, size=(300, 100))],
        [sg.Button("Calculate"), sg.Button("Submit"), sg.Button("Cancel")],
        [sg.Text("Total Payment: $0", key="-TOTAL_PAYMENT-")]
    ]

    window = sg.Window("New Membership", layout)

    # Event loop for the new membership form window
    while True:
        event, values = window.read()
        if event == "Calculate":
            # Calculate the total payment based on selected options
            total_payment = 0
            for i, extra in enumerate(extras_options):
                if f"-EXTRA-{i}-" in values and values[f"-EXTRA-{i}-"]:
                    price = int(extra.split("$")[1].split("pw")[0])
                    total_payment += price

            window["-TOTAL_PAYMENT-"].update(f"Total Payment: ${total_payment}")

        elif event == "Submit":
            # Get the form values
            first_name = values["-FIRST_NAME-"].strip()
            last_name = values["-LAST_NAME-"].strip()
            address = values["-ADDRESS-"].strip()
            phone_number = values["-PHONE_NUMBER-"].strip()
            membership_type = values["-MEMBERSHIP_TYPE-"]
            duration = values["-DURATION-"]

            selected_extras = [
                extras_options[i] for i, checked in enumerate(values.values())
                if f"-EXTRA-{i}-" in values and checked
            ]

            # Perform basic error checks
            if not first_name:
                sg.popup("Please enter a first name.")
                continue
            if not last_name:
                sg.popup("Please enter a last name.")
                continue
            if not address:
                sg.popup("Please enter an address.")
                continue
            if not phone_number:
                sg.popup("Please enter a phone number.")
                continue

            # Create a tuple with the data to be inserted
            member_data = (first_name, last_name, address, phone_number, membership_type, ", ".join(selected_extras), total_payment)

            # Insert the member data into the database
            insert_member_data(member_data)

            window.close()
            break
        elif event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break

    # Close the database connection
    conn.close()

def search_members(search_criteria):
    try:
        cursor.execute("""
            SELECT * FROM Members
            WHERE first_name LIKE ? OR last_name LIKE ? OR address LIKE ? OR mobile_number LIKE ?
        """, search_criteria)
        members_data = cursor.fetchall()
        if len(members_data) == 0:
            sg.popup("No records found for the search criteria.")
        else:
            # Display the retrieved information (format as per your choice)
            for member in members_data:
                sg.popup(f"Member ID: {member[0]}\nFirst Name: {member[1]}\nLast Name: {member[2]}\nAddress: {member[3]}\nMobile Number: {member[4]}\nPayment Frequency: {member[5]}\nExtras: {member[6]}\nRegular Payment: {member[7]}")
    except sqlite3.Error as e:
        sg.popup("Error occurred while searching members:", str(e))

def search_members_form():
    layout = [
        [sg.Text("Search Members")],
        [sg.Text("Last Name:"), sg.Input(key="-SEARCH_TEXT-")],
        [sg.Button("Search"), sg.Button("Cancel")],
        [sg.Text("Results:")],
        [sg.Output(size=(60, 10), key="-RESULTS-")]
    ]

    window = sg.Window("Search Members", layout)

    while True:
        event, values = window.read()
        if event == "Search":
            # Get the search criteria
            search_text = values["-SEARCH_TEXT-"].strip()

            # Perform the search based on the criteria
            search_criteria = (f"%{search_text}%", f"%{search_text}%", f"%{search_text}%", f"%{search_text}%")
            search_members(search_criteria)
            
        elif event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break

# Close the database connection
conn.close()

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
        [sg.Text("- Click 'Submit' to save the membership details.")],
        [sg.Text("- Click 'Cancel' to exit the form without saving.")],
        [sg.Text("")],
        [sg.Text("Search Members Form:")],
        [sg.Text("- Enter the last name of the member you want to search for.")],
        [sg.Text("- Click 'Search' to display the matching results.")],
        [sg.Text("- Click 'Cancel' to exit the form.")],
        [sg.Text("")],
        [sg.Text("Fitness Class Enrollment Form:")],
        [sg.Text("- Select the fitness class from the dropdown list.")],
        [sg.Text("- Enter the last name of the member to enroll.")],
        [sg.Text("- Click 'Enroll' to complete the enrollment.")],
        [sg.Text("- Click 'Cancel' to exit the form.")],
        [sg.Text("")],
        [sg.Button("Close")]
    ]

    window = sg.Window("Help", layout)

    while True:
        event, values = window.read()
        if event == "Close" or event == sg.WIN_CLOSED:
            window.close()
            break

# Main Application Loop
def main():
    menu_def = [
        ["File", ["New Membership", "Search Members", "Exit"]],
        ["Fitness", ["Fitness Class Enrollment"]],
        ["Help", ["Help"]]
    ]

    layout = [
        [sg.Menu(menu_def, tearoff=False)],
        [sg.Text("Welcome to the Gym Membership Application!", font=("Arial", 16))]
    ]

    window = sg.Window("Gym Membership Application", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        elif event == "New Membership":
            new_membership_form()
        elif event == "Search Members":
            search_members_form()
        elif event == "Fitness Class Enrollment":
            fitness_form()
        elif event == "Help":
            help_screen()

    window.close()

if __name__ == "__main__":
    main()
