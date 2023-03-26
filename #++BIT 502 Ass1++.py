import time as t
def cal_bmi():
    '''
    simple bmi calculation for new customers
    bmi=weight/height**2
    '''
    print('--------------------------------------------------------------')
    print('---Enter 1 to start bmi calculation---')
    print('---Enter 2 to go back to the main menu---')
    print('--------------------------------------------------------------')
    start = input('')

    def bmi_input():
        global input_weight_float, input_height_float
        if start == '1':
            try:
                print('Welcome to the City Gym Body Mass Index (BMI) calculator')
                print('--------------------------------------------------------------')
                t.sleep(2)
                print('We will now ask you to enter a series of body stats')
                print('--------------------------------------------------------------')
                t.sleep(2)
                print('Please enter numbers, either whole i.e 10 or decimal i.e 10.55')
                print('--------------------------------------------------------------')
                t.sleep(2)
                print('Enter 2 at any time to go back to the main menu')
                print('--------------------------------------------------------------')
                t.sleep(2)
                print('--------------------------------------------------------------')
                print('Enter your weight in Kgs')
                print('--------------------------------------------------------------')
                t.sleep(1)
                input_weight_str = input('')
                if input_weight_str == '2':
                    main_menu()
                else:
                    print('Enter your height in Meters')
                    print('--------------------------------------------------------------')
                    t.sleep(1)
                    input_height_str = input('')
                if input_height_str == 2:
                    main_menu()
                else:
                    input_weight_float = float(input_weight_str)
                    input_height_float = float(input_height_str)
            except ValueError as e:
                print('!Incorrect input, please enter an interger or float number!')
                print('--------------------------------------------------------------')
                t.sleep(1)
                print('restating BMI calculator')
                print('--------------------------------------------------------------')
                t.sleep(1)
                bmi_input()
        elif start == 2:
                main_menu()
        else:
            print('!Incorrct input, please try again!')
            bmi_input()

    bmi_input()
    bmi_height = input_height_float * input_height_float
    bmi = input_weight_float / bmi_height 
    bmi_result = None
    try:
        if bmi < 18.5:
            bmi_result = 'Underweight'
        elif bmi >= 18.5 < 25:
            bmi_result = 'Normal'
        elif bmi >= 25 < 30:
            bmi_result = 'Overweight'
        elif bmi >= 30:
            bmi_result = 'Obese'
    except TypeError as e:
            print('Incorrct input, please input weight in kg and height as numbers')
            cal_bmi()
    str_bmi = str(bmi)
    print('Your BMI is ' + str_bmi)
    print('You are classed as ' + bmi_result)
    yield(bmi_result)
    print('Loading main menu...')
    main_menu()
    
def membership_rate():
    '''
    Menu to allow selection of memebership rates
    '''
    basic_rate = '$10 per week'
    regular_rate = '$15 per week'
    premium_rate = '$20 per week'
    back = 'back to the main menu'
    mem_menu = {
        '1' : basic_rate,
        '2' : regular_rate,
        '3' : premium_rate,
        '4' : back
    }
    print('City Gym membership rates')
    print('--------------------------------------------------------------')
    for key, value in mem_menu.items():
        print(key, ' -- ', value)
    print('--------------------------------------------------------------')
    print('Please select a membership option from the above')
    
    try:
        selection = input('')
        if selection == 'back to the main menu':
            main_menu()
        else:
            selection_int = int(selection)
        mem_selection = mem_menu[selection_int]
    except KeyError as e:
        print('Incorect input please try again i.e 1,2,3')
        membership_rate()

    yield(mem_selection)
    main_menu()

def exit():
    '''
    Simple python script exit
    '''
    
    print('--------------------------------------------------------------')
    print('Enter any key to exit the application')
    print('--------------------------------------------------------------')
    exit = input('')
    exit1 = bool(exit)

    if exit1 == True:
        import sys
        sys.exit()

def main_menu():
    '''
    Main menu allows for selection of application functions
    '''
    menu = {
        '1': 'Calculate body mass index (BMI)',
        '2': 'View membership rates',
        '3': 'Exit'
    }

    def menu_selection():
        '''
        Prints the app function menu, runs logic for selection
        '''
        def input_check():
            '''
            Input for menu selection plus error check 
            '''
            global main_option_int
            main_option_str = input('')
            try:
                main_option_int = int(main_option_str)
            except ValueError as e:
                print('Invalid value, Please enter an integer')
                input_check()
        print('--------------------------------------------------------------')
        for key, value in menu.items():
            print(key, ' -- ', value)
        print('--------------------------------------------------------------')
        input_check()

        '''if option == int:
            option_int = int(option)
        elif option != int:
            print('Invalid option, Please enter number assocatited with option')
            menu_selection()'''
        
        try:
            if main_option_int == '1':
                cal_bmi()
            elif main_option_int == '2':
                membership_rate()
            elif main_option_int == '3':
                exit()
            else:
                print('Invalid option, Please enter number assocatited with option')
                menu_selection()
        except KeyError as e:
            print('Incorrect input, please enter an option number')
            menu_selection()
    print('--------------------------------------------------------------')
    print('        -- Welcome to the City Gym App main menu! --')
    print('--------------------------------------------------------------')
    while (True):
        menu_selection()

main_menu()
