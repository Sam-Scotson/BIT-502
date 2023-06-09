import PySimpleGUI as sg

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

            # Handle form submission logic here
            print(f"First Name: {first_name}")
            print(f"Last Name: {last_name}")
            print(f"Address: {address}")
            print(f"Phone Number: {phone_number}")
            print(f"Membership Type: {membership_type}")
            print(f"Membership Duration: {duration}")
            print("Selected Extras:")
            for extra in selected_extras:
                print(f"- {extra}")

            window.close()
            break
        elif event == "Cancel" or event == sg.WIN_CLOSED:
            window.close()
            break