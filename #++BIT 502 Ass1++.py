#++BIT 502 Ass1++

def cal_bmi():
    """
    simple bmi calculation for new customers
    bmi=weight/height**2
    """
    print("--------------------------------------------------------------")
    print("Enter any key to begin bmi calculation")
    print("--------------------------------------------------------------")
    start = input("")
    start1 = bool(start)

    if start1 == True:
        try:
            print("Enter your weight as number/kg")
            input_weight_str = input("")
            print("Enter your height as number/meter")
            input_height_str = input("")

            input_weight_float = float(input_weight_str)
            input_height_float = float(input_height_str)

            bmi_height = input_height_float * input_height_float
            bmi = input_weight_float / bmi_height 
            bmi_result = None
    
            if bmi < 18.5:
                bmi_result = "Underweight"
            elif bmi >= 18.5 < 25:
                bmi_result = "Normal"
            elif bmi >= 25 < 30:
                bmi_result = "Overweight"
            elif bmi >= 30:
                bmi_result = "Obese"
        except TypeError as e:
            print('Incorrct input, please input weight in kg and height as numbers')
            cal_bmi()
    str_bmi = str(bmi)
    print('Your BMI is ' + str_bmi)
    print('You are classed as ' + bmi_result)
    return(bmi_result)

def membership_rate():
    """
    Menu to allow selection of memebership rates
    """
    basic_rate = '$10 per week'
    regular_rate = '$15 per week'
    premium_rate = '$20 per week'

    mem_menu = {
        '1' : basic_rate,
        '2' : regular_rate,
        '3' : premium_rate
    }
    print("City Gym membership rates")
    print("--------------------------------------------------------------")
    for key, value in mem_menu.items():
        print(key, ' -- ', value)
    print("--------------------------------------------------------------")
    print('Please select a membership option from the above')

    try:
        selection = input('')
        mem_selection = mem_menu[selection]
    except KeyError as e:
        print("Incorect input please try again i.e 1,2,3")
        membership_rate()
    return(mem_selection)

def exit():
    """
    Simple python script exit
    """
    print("--------------------------------------------------------------")
    print("Enter any key to exit the application")
    print("--------------------------------------------------------------")
    exit = input("")
    exit1 = bool(exit)

    if exit1 == True:
        quit()

def main_menu():
    """
    Main menu allows for selection of application functions
    """
    menu = {
        '1': "Calculate body mass index (BMI)",
        '2': "View membership rates",
        '3': "Exit"
    }

    def menu_selection():
        """
        Prints the app function menu, runs logic for selection
        """
        def input_check():
            """
            Input for menu selection plus error check 
            """
            global main_option_int
            main_option_str = input('')
            try:
                main_option_int = int(main_option_str)
            except ValueError as e:
                print('Invalid value, Please enter an integer')
                input_check()
        print("--------------------------------------------------------------")
        for key, value in menu.items():
            print(key, ' -- ', value)
        print("--------------------------------------------------------------")
        input_check()

        #if option == int:
        #    option_int = int(option)
        #elif option != int:
        #    print('Invalid option, Please enter number assocatited with option')
        #    menu_selection()
        
        try:
            if main_option_int == 1:
                cal_bmi()
            elif main_option_int == 2:
                membership_rate()
            elif main_option_int == 3:
                exit()
            else:
                print('Invalid option, Please enter number assocatited with option')
                menu_selection()
        except KeyError as e:
            print("Incorrect input, please enter an option number")
            menu_selection()

    print("--------------------------------------------------------------")
    print("        -- Welcome to the City Gym App main menu! --")
    print("--------------------------------------------------------------")
    while (True):
        menu_selection()

main_menu()















#//////////////////////////

#  
    print("----------------------------------")
    print("Press 1) Calculate body mass index (BMI)")
    print("Press 2) View membership cost")
    print("Press 3) Exit")
    print("----------------------------------")
    option = input()
    menu_selection()



    menu_input = input("Please select from the available options")

    try:
        menu[menu_input]
    except KeyError as e:
        print("Invalid selection, please try again")
        menu_input = input("Please select from the available options")


def main():




main()
