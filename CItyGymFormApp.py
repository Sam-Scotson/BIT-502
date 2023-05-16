from guizero import App, ListBox, Picture, Text, TextBox,PushButton, ButtonGroup, CheckBox, Window, Box

def gym_app():
    '''
     main guizero code block, sets up the app gui grid and calls/modifies/places the widgets
    Args:
     none
    Returns:
     an interactive gui
    '''
    global infoList 
    #infoList - main list that is used to gather all inputs from gui widgets into a data structure 
    infoList = ["Customer Sign-up Info",]
    but_hex = "#7B61FF"
    but_hex_light = "#c5b9ff"

    app = App(title="City Gym", height=1200, width=600, layout="grid")

    picture = Picture(app, image="citygymlogo.png", grid=[1,0])

    text1 = Text(app, text="City Gym", grid=[1,1])
    text2 = Text(app, text="Membership Form", grid=[1,2])
    text3 = Text(app, text="CUSTOMER DETAILS", grid=[1,3])
    global textboxFirst, textboxLast, textboxAddress, textboxNumber
    textboxFirst = TextBox(app, text="First name", grid=[1,4], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,5], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,6], width=20)
    textboxNumber = TextBox(app, text="Mobile number", grid=[1,7], width=20)

    def personal_info():
        '''
         widget function: checks if personal info has been added to the infoList or if defaults are still in field
         if not the new completed fields are added to infoList
        '''
        if textboxFirst.value.isdigit == True:
            print('only use alphabetic characters')
            pass
        if textboxLast.value.isdigit == True:
            print('only use alphabetic characters')
            pass
        elif "First name" in textboxFirst.value:
            print('please fill all fields')
            pass
        elif "Last name" in textboxLast.value:
            print('please fill all fields')
            pass
        elif "Address" in textboxAddress.value:
            print('please fill all fields')
            pass
        elif "Mobile number" in textboxNumber.value:
            print('please fill all fields')
            pass
        else:
            infoList.extend([
            "Personal Info",
            "First Name: " + str(textboxFirst.value), 
            "Last Name: " + str(textboxLast.value),
            "Address: " + str(textboxAddress.value),
            "Mobile Number: " + str(textboxNumber.value),
            ])
            listBox.append("First Name: " + str(textboxFirst.value))
            listBox.append("Last Name: " + str(textboxLast.value))
            listBox.append("Address: " + str(textboxAddress.value))
            listBox.append("Mobile Number: " + str(textboxNumber.value))
            thxText = Text(app, text="Thank you!", grid=[1,9], visible=True)
    global button
    button = PushButton(app, text="Enter", command=personal_info, grid=[1,8])
    button.bg = but_hex

    text5 = Text(app, text="", grid=[1,10])
    text6 = Text(app, text="MEMBERSHIP DETAILS", grid=[1,10])
    text7 = Text(app, text="Membership Type", grid=[1,11])

    box = Box(app, layout="grid", grid=[1,12])

    def mem_type_10():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not basic membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            pass
        elif "Membership Type: Regular $15pw" in infoList:
            [s.replace("Membership Type: Regular $15pw", "Membership Type: Basic $10pw") for s in infoList]
        elif "Membership Type: Premium $20pw" in infoList: 
            [s.replace("Membership Type: Premium $20pw", "Membership Type: Basic $10pw") for s in infoList]
        else:
            infoList.append("Membership Type: Basic $10pw")
    global button1
    button1 = PushButton(box, text="Basic $10pw", command=mem_type_10, grid=[0,1])
    button1.bg = but_hex

    def mem_type_15():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not regular membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            [s.replace("Membership Type: Basic $10pw", "Membership Type: Regular $15pw") for s in infoList]
        elif "Membership Type: Regular $15pw" in infoList:
            pass
        elif "Membership Type: Premium $20pw" in infoList: 
            [s.replace("Membership Type: Premium $20pw", "Membership Type: Regular $15pw") for s in infoList]
        else:
            infoList.append("Membership Type: Regular $15pw")
    global button2
    button2 = PushButton(box, text="Regular $15pw", command=mem_type_15, grid=[1,1])
    button2.bg = but_hex

    def mem_type_20():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not premium membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            [s.replace("Membership Type: Basic $10pw", "Membership Type: Premium $20pw") for s in infoList]
        elif "Membership Type: Regular $15pw" in infoList:
            [s.replace("Membership Type: Regular $15pw", "Membership Type: Premium $20pw") for s in infoList]
        elif "Membership Type: Premium $20pw" in infoList: 
            pass
        else:
            infoList.append("Membership Type: Premium $20pw")
    global button3
    button3 = PushButton(box, text="Premium $20pw", command=mem_type_20, grid=[2,1])
    button3.bg = but_hex
    
    text8 = Text(app, text="Membership Duration", grid=[1,13])
    
    box1 = Box(app, layout="grid", grid=[1,14])

    def mem_dur_3():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 3 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            pass
        elif "Duration: 12 Months" in infoList:
            [s.replace("Duration: 12 Months", "Duration: 3 Months") for s in infoList]
        elif "Duration: 24 Months" in infoList: 
            [s.replace("Duration: 24 Months", "Duration: 3 Months") for s in infoList]
        else:
            infoList.append("Duration: 3 Months")
    global button4
    button4 = PushButton(box1, text="3 Months", command=mem_dur_3, grid=[0,1])
    button4.bg = but_hex

    def mem_dur_12():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 12 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            [s.replace("Duration: 3 Months", "Duration: 12 Months") for s in infoList]
        elif "Duration: 12 Months" in infoList:
            pass
        elif "Duration: 24 Months" in infoList: 
            [s.replace("Duration: 24 Months", "Duration: 12 Months") for s in infoList]
        else:
            infoList.append("Duration: 12 Months")
    global button5
    button5 = PushButton(box1, text="12 Months", command=mem_dur_12, grid=[1,1])
    button5.bg = but_hex

    def mem_dur_24():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 24 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            [s.replace("Duration: 3 Months", "Duration: 24 Months") for s in infoList]
        elif "Duration: 12 Months" in infoList:
            [s.replace("Duration: 12 Months", "Duration: 24 Months") for s in infoList]
        elif "Duration: 24 Months" in infoList: 
            pass
        else:
            infoList.append("Duration: 24 Months")
    global button6
    button6 = PushButton(box1, text="24 Months", command=mem_dur_24, grid=[2,1])
    button6.bg = but_hex 

    text9 = Text(app, color=but_hex, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,15])
    text10 = Text(app, text="", grid=[1,15])

    text11 = Text(app, text="PAYMENT OPTIONS", grid=[1,16])
    text12 = Text(app, text="Direct Debt", grid=[1,17])

    def direct_credit():
        '''
         widget function: checks if payment option has been added to the infoList
         if not a check on which postion the buttongroup is on and adds the selection to infoList
        '''
        if "Direct Debit: Yes" in infoList:
            [s.replace("Direct Debit: Yes", "Direct Debit: No") for s in infoList]
        elif "Direct Debit: No" in infoList:
            [s.replace("Direct Debit: No", "Direct Debit: Yes") for s in infoList]
        else:
            if groupButton1.value == 1:
                infoList.append("Direct Debit: Yes")
            elif groupButton1.value == 0:
                infoList.append("Direct Debit: No")
    global groupButton1
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected=None, command=direct_credit, grid=[1,18])
    groupButton1.bg = but_hex_light

    text13 = Text(app, text="Frequecncy of payments", grid=[1,19])

    def frq_payment():
        '''
         widget function: checks if payment freq option has been added to the infoList
         if not a check on which postion the buttongroup is on and adds the selection to infoList
        '''
        if "Frequecncy of Payments: Weekly" in infoList:
            [s.replace("Frequecncy of Payments: Weekly", "Frequecncy of Payments: Monthly") for s in infoList]
        elif "Frequecncy of Payments: Monthly" in infoList:
            [s.replace("Frequecncy of Payments: Monthly", "Frequecncy of Payments: Weekly") for s in infoList]
        else:
            if groupButton2.value == 1:
                infoList.append("Frequecncy of Payments: Weekly")
            elif groupButton2.value == 0:
                infoList.append("Frequecncy of Payments: Monthly")
    global groupButton2
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected=None, command=frq_payment, grid=[1,20])
    groupButton2.bg = but_hex_light

    text14 = Text(app, text="", grid=[1,21])
    window = Window(app, height=1200, width=300, layout="grid")
    text15 = Text(window, text="EXTRAS", grid=[1,1])
    global listBox
    #listBox - gui element, updates as infomation is entered into the gui
    listBox = ListBox(window, items=[infoList], grid=[1,10])
    listBox.bg = but_hex_light
    def extra_24():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            [s.replace("Extra(24/7 Access): Yes", "Extra(24/7 Access): No") for s in infoList]
        elif "Extra(24/7 Access): No" in infoList:
            [s.replace("Extra(24/7 Access): No", "Extra(24/7 Access): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(24/7 Access): Yes" not in infoList:
                    infoList.append("Extra(24/7 Access): Yes")
            elif checkBox1.value == 0:
                if "Extra(24/7 Access): No" not in infoList:
                    infoList.append("Extra(24/7 Access): No")
    global checkBox1
    checkBox1 = CheckBox(window, text="24/7 Access/$1pw", command=extra_24, grid=[1,2])
    checkBox1.bg = but_hex_light

    def extra_trainer():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Personal Trainer/$20pw): Yes" in infoList:
            [s.replace("Extra(Personal Trainer/$20pw): Yes", "Extra(Personal Trainer/$20pw): No") for s in infoList]
        elif "Extra(Personal Trainer/$20pw): No" in infoList:
            [s.replace("Extra(Personal Trainer/$20pw): No", "Extra(Personal Trainer/$20pw): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Personal Trainer/$20pw): Yes" not in infoList:
                    infoList.append("Extra(Personal Trainer/$20pw): Yes")
            elif checkBox1.value == 0:
                if "Extra(Personal Trainer/$20pw): No" not in infoList:
                    infoList.append("Extra(Personal Trainer/$20pw): No")
    global checkBox2
    checkBox2 = CheckBox(window, text="Personal Trainer/$20pw", command=extra_trainer, grid=[1,3])
    checkBox2.bg = but_hex_light

    def extra_diet():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Diet Consultation/$20pw): Yes" in infoList:
            [s.replace("Extra(Diet Consultation/$20pw): Yes", "Extra(Diet Consultation/$20pw): No") for s in infoList]
        elif "Extra(Diet Consultation/$20pw): No" in infoList:
            [s.replace("Extra(Diet Consultation/$20pw): No", "Extra(Diet Consultation/$20pw): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Diet Consultation/$20pw): Yes" not in infoList:
                    infoList.append("Extra(Diet Consultation/$20pw): Yes")
            elif checkBox1.value == 0:
                if "Extra(Diet Consultation/$20pw): No" not in infoList:
                    infoList.append("Extra(Diet Consultation/$20pw): No")
    global checkBox3
    checkBox3 = CheckBox(window, text="Diet Consultation/$20pw", command=extra_diet, grid=[1,4])
    checkBox3.bg = but_hex_light

    def extra_video():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Online Fitness Videos/$2pw): Yes" in infoList:
            [s.replace("Extra(Online Fitness Videos/$2pw): Yes", "Extra(Online Fitness Videos/$2pw): No") for s in infoList]
        elif "Extra(Online Fitness Videos/$2pw): No" in infoList:
            [s.replace("Extra(Online Fitness Videos/$2pw): No", "Extra(Online Fitness Videos/$2pw): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Online Fitness Videos/$2pw): Yes" not in infoList:
                    infoList.append("Extra(Online Fitness Videos/$2pw): Yes")
            elif checkBox1.value == 0:
                if "Extra(Online Fitness Videos/$2pw): No" not in infoList:
                    infoList.append("Extra(Online Fitness Videos/$2pw): No")
    global checkBox4
    checkBox4 = CheckBox(window, text="Online Fitness Videos/$2pw", command=extra_video, grid=[1,5])
    checkBox4.bg = but_hex_light

    text16 = Text(window, text="", grid=[1,6])
    text17 = Text(window, text="PAYMENT TOTAL", grid=[1,7])
    text18 = Text(window, text="", grid=[1,8])

    def calculate_button():
        '''
        a collection of fuctions to calculate the total payment, lists varibles of options and executes functions
        Args:
        infoList
        Returns:
        the regular payment data
        '''
        def base_mem():
            '''
            sub-function checks which membership is in the infoList and charges the assocecatied to a varible to be calculated later 
            Args:
            baseMem, infoList
            Returns:
            none
            '''
            global baseMem 
            baseMem = 0
            if "Membership Type: Basic $10pw" in infoList:
                baseMem += 10
            elif "Membership Type: Regular $15pw" in infoList:
                baseMem += 15
            elif "Membership Type: Premium $20pw" in infoList:
                baseMem += 20
            else:
                print('error, restarting app')

        def dur_mem():
            '''
            sub-function checks which membership is in the infoList and charges the assocecatied to a varible to be calculated later 
            Args:
            durMem, infoList
            Returns:
            none
            '''
            global durMem
            durMem = 0
            if "Duration: 3 Months" in infoList:
                durMem += 0
            elif "Duration: 12 Months" in infoList:
                durMem += -2
            elif "Duration: 24 Months" in infoList:
                durMem += -5
            else:
                print('error, restarting app')
            return(durMem)

        def pay_mem():
            '''
            sub-function checks if either yes or no for direct payment and subtracts a 1% discount from total
            Args:
            baseMem, infoList
            Returns:
            none
            '''
            global disMem
            disMem = 0
            if "Direct Debit: Yes" in infoList:
                disMem = 1 * baseMem/100
            elif "Direct Debit: No" in infoList:
                pass
            return(disMem)

        def extra_mem(perWeek):
            '''
            sub-function checks which of the extra options if any are in infoList and adds the asscoitated options varible to the total  
            Args:
            perWeek, infoList
            Returns:
            none
            '''
            if "Extra(24/7 Access): Yes" in infoList:
                perWeek += 1
            if "Extra(Personal Trainer): Yes" in infoList:
                perWeek += 20
            if "Extra(Diet Consultation): Yes" in infoList:
                perWeek += 20
            if "Extra(Online Fitness Videos): Yes" in infoList:
                perWeek += 2
            return(perWeek)

        def frq_mem(exPerWeek):
            '''
            sub-function checks if either weekly or monthly are selected from the infoList and adjusts the regular payment
            Args:
            perWeek,regularPay,infoList
            Returns:
            regularPay
            '''
            if "Frequecncy of Payments: Weekly" in infoList:
                regularPay = exPerWeek
                infoList.append("regular payments: " + str(regularPay)) 
            elif "Frequecncy of Payments: Monthly" in infoList:
                regularPay = exPerWeek * 4
                infoList.append("regular payments: " + str(regularPay)) 

        global baseMem, durMem, disMem
        base_mem()
        dur_mem()
        pay_mem()
        global perWeek
        perWeek = (baseMem - disMem) + durMem
        exPerWeek = extra_mem(perWeek)
        frq_mem(exPerWeek)
    cal_button = PushButton(window, text="Calculate Membership", command=calculate_button, grid=[1,9])
    cal_button.bg = but_hex


    def text_output_customer_info():
        '''
         outputs the new client infolist as a text file
        Args:
         infoList
        Returns:
         none
        '''
        with open('membersdatasaved.txt', 'w') as f:
            for values in infoList:
                f.write(values + "\n")
        f.close()
        infoList.append('finished')
        import sys
        if 'finished' in infoList:
            sys.exit()
    submit_button = PushButton(window, text="Submit and Exit", command=text_output_customer_info, grid=[1,11])
    submit_button.bg = but_hex_light

    app.display() 

gym_app()

#////////////DEBUG KIT//////////////////
import os
os.chdir(f'C:/Users/Sam/Documents/OpenPoly/BIT502Ass2')
infoList = [
    "Membership Type: Basic $10pw",
    "Duration: 12 Months",
    "Extra(24/7 Access): Yes"
    "Extra(Personal Trainer): Yes",
    "Extra(Diet Consultation): Yes",
    "Extra(Online Fitness Videos): Yes",
    "Direct Debit: Yes",
    "Frequecncy of Payments: Monthly",
    "Regular Payments: " 
]
