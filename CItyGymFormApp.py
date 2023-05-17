from guizero import *

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
    infoList = []
    but_hex = "#7B61FF"
    but_hex_light = "#c5b9ff"

    app = App(title="City Gym", height=1200, width=650, layout="grid", bg="#36332e")

    picture = Picture(app, image="citygymlogo.png", grid=[1,0])
    text1 = Text(app, text="City Gym Membership Form", grid=[1,1])
    text3 = Text(app, text="CUSTOMER DETAILS", grid=[1,2])
    global textboxFirst, textboxLast, textboxAddress, textboxNumber
    textboxFirst = TextBox(app, text="First name", grid=[1,3], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,4], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,5], width=20)
    textboxNumber = TextBox(app, text="Mobile number", grid=[1,6], width=20)

    def personal_info():
        '''
         widget function: checks if personal info has been added to the infoList or if defaults are still in field
         if not the new completed fields are added to infoList
        '''
        if '1' in textboxFirst.value or '2' in textboxFirst.value or '3' in textboxFirst.value or '4' in textboxFirst.value or '5' in textboxFirst.value or '6' in textboxFirst.value or '7' in textboxFirst.value or '8' in textboxFirst.value or '9' in textboxFirst.value or '0' in textboxFirst.value:
            text51.clear()
            text51.append('only use alphabetic characters')
            pass
        if '1' in textboxLast.value or '2' in textboxLast.value or '3' in textboxLast.value or '4' in textboxLast.value or '5' in textboxLast.value or '6' in textboxLast.value or '7' in textboxLast.value or '8' in textboxLast.value or '9' in textboxLast.value or '0' in textboxLast.value:
            text51.clear()
            text51.append('only use alphabetic characters')
            pass
        elif "First name" in textboxFirst.value:
            text51.clear()
            text51.append('please fill all fields')
            pass
        elif "Last name" in textboxLast.value:
            text51.clear()
            text51.append('please fill all fields')
            pass
        elif "Address" in textboxAddress.value:
            text51.clear()
            text51.append('please fill all fields')
            pass
        elif "Mobile number" in textboxNumber.value:
            text51.clear()
            text51.append('please fill all fields')
            pass
        else:
            if "Customer Sign-up Info" in infoList:
                pass
            else:
                text51.clear()
                infoList.extend([
                "Customer Sign-up Info",
                "First Name: " + str(textboxFirst.value), 
                "Last Name: " + str(textboxLast.value),
                "Address: " + str(textboxAddress.value),
                "Mobile Number: " + str(textboxNumber.value),
                ])
    text51 = Text(app, text='', grid=[1,7])
    global button
    button = PushButton(app, text="Enter", command=personal_info, grid=[1,8], height=1)
    button.bg = but_hex

    text6 = Text(app, text="MEMBERSHIP DETAILS", grid=[1,9])
    text7 = Text(app, text="Membership Type", grid=[1,10])

    box = Box(app, layout="grid", grid=[1,11])

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
    
    text8 = Text(app, text="Membership Duration", grid=[1,12])
    text9 = Text(app, color=but_hex, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,13])

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


    text11 = Text(app, text="PAYMENT OPTIONS", grid=[1,15])
    text12 = Text(app, text="Direct Debt", grid=[1,16])
    text121 = Text(app, color=but_hex, text='For direct debits, there is a 1% discount on the base membership cost.', grid=[1,17])

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
            if groupButton1.value == 'Yes':
                infoList.append("Direct Debit: Yes")
            elif groupButton1.value == 'No':
                infoList.append("Direct Debit: No")
    global groupButton1
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected="Yes", command=direct_credit, grid=[1,18])
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
            if groupButton2.value == 'Weekly':
                infoList.append("Frequecncy of Payments: Weekly")
            elif groupButton2.value == 'Monthly':
                infoList.append("Frequecncy of Payments: Monthly")
    global groupButton2
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected="Weekly", command=frq_payment, grid=[1,20])
    groupButton2.bg = but_hex_light

   # window = Window(app, height=1200, width=300, layout="grid")
    text15 = Text(app, text="EXTRAS", grid=[1,21])

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
    checkBox1 = CheckBox(app, text="24/7 Access/$1pw", command=extra_24, grid=[1,22])
    checkBox1.bg = but_hex_light

    def extra_trainer():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Personal Trainer): Yes" in infoList:
            [s.replace("Extra(Personal Trainer): Yes", "Extra(Personal Trainer): No") for s in infoList]
        elif "Extra(Personal Trainer): No" in infoList:
            [s.replace("Extra(Personal Trainer): No", "Extra(Personal Trainer): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Personal Trainer): Yes" not in infoList:
                    infoList.append("Extra(Personal Trainer): Yes")
            elif checkBox1.value == 0:
                if "Extra(Personal Trainer): No" not in infoList:
                    infoList.append("Extra(Personal Trainer): No")
    global checkBox2
    checkBox2 = CheckBox(app, text="Personal Trainer/$20pw", command=extra_trainer, grid=[1,23])
    checkBox2.bg = but_hex_light

    def extra_diet():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Diet Consultation): Yes" in infoList:
            [s.replace("Extra(Diet Consultation): Yes", "Extra(Diet Consultation): No") for s in infoList]
        elif "Extra(Diet Consultation): No" in infoList:
            [s.replace("Extra(Diet Consultation): No", "Extra(Diet Consultation): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Diet Consultation): Yes" not in infoList:
                    infoList.append("Extra(Diet Consultation): Yes")
            elif checkBox1.value == 0:
                if "Extra(Diet Consultation): No" not in infoList:
                    infoList.append("Extra(Diet Consultation): No")
    global checkBox3
    checkBox3 = CheckBox(app, text="Diet Consultation/$20pw", command=extra_diet, grid=[1,24])
    checkBox3.bg = but_hex_light

    def extra_video():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(Online Fitness Videos): Yes" in infoList:
            [s.replace("Extra(Online Fitness Videos): Yes", "Extra(Online Fitness Videos): No") for s in infoList]
        elif "Extra(Online Fitness Videos): No" in infoList:
            [s.replace("Extra(Online Fitness Videos): No", "Extra(Online Fitness Videos): Yes") for s in infoList]
        else:
            if checkBox1.value == 1:
                if "Extra(Online Fitness Videos): Yes" not in infoList:
                    infoList.append("Extra(Online Fitness Videos): Yes")
            elif checkBox1.value == 0:
                if "Extra(Online Fitness Videos): No" not in infoList:
                    infoList.append("Extra(Online Fitness Videos): No")
    global checkBox4
    checkBox4 = CheckBox(app, text="Online Fitness Videos/$2pw", command=extra_video, grid=[1,25])
    checkBox4.bg = but_hex_light

    def calculate_button():
        '''
         a list of if statements to check against the main infoList, if statements add or subtract based on the options inside the infoList
         at the end a error check is done to make sure there are no duplicates and a regular payment sum is added to the infoList
        Args:
         infoList
        Returns:
         the regular payment data
        '''
        global payment
        global reguarpayment
        reguarpayment = 0
        payment = 0
        baseMem = 0
        listBox.clear()
        if 'Membership Type: Basic $10pw' in infoList:
            reguarpayment += 10
            baseMem += 10
        elif 'Membership Type: Regular $15pw' in infoList:
            reguarpayment += 15
            baseMem += 15
        elif 'Membership Type: Premium $20pw' in infoList:
            reguarpayment += 20
            baseMem += 20

        if 'Duration: 3 Months' in infoList:
            reguarpayment += 0
        elif 'Duration: 12 Months' in infoList:
            reguarpayment += -2
        elif 'Duration: 24 Months' in infoList:
            reguarpayment += -5

        if 'Direct Debit: Yes' in infoList:
            disMem = 1 * baseMem/100
            reguarpayment -= disMem
        elif 'Direct Debit: No' in infoList:
            pass

        if 'Extra(24/7 Access): Yes' in infoList:
            reguarpayment += 1
        elif 'Extra(Personal Trainer): Yes' in infoList:
            reguarpayment += 20
        elif 'Extra(Diet Consultation): Yes' in infoList:
            reguarpayment += 20
        elif 'Extra(Online Fitness Videos): Yes' in infoList:
            reguarpayment += 2

        if 'Frequecncy of Payments: Weekly' in infoList:
            payment = reguarpayment
        elif 'Frequecncy of Payments: Monthly' in infoList:
            payment = reguarpayment * 4
        
        if [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,] or [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("regular payments:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1]:
            infoList.append('regular payments: ' + str(payment)) 
            listBox.append('regular payments: ' + str(payment))

    cal_button = PushButton(app, text="Calculate Membership", command=calculate_button, grid=[1,26])
    cal_button.bg = but_hex

    text17 = Text(app, text="PAYMENT TOTAL", grid=[1,27])
    global listBox
    #listBox - gui element, updates as infomation is entered into the gui
    listBox = ListBox(app, items=[], grid=[1,28], width=200, height=30)
    listBox.bg = but_hex_light


    def text_output_customer_info():
        '''
         outputs the new client infolist as a text file
        Args:
         infoList
        Returns:
         none
        '''
        if "Customer Sign-up Info" not in infoList:
            text18 = Text(app, text='Please fill and select all options before submitting', grid=[1,30])
            pass
        elif [s.find("Membership Type:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Membership Type:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,] or [s.find("Membership Type:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Membership Type:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Membership Type:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1]:
            text18 = Text(app, text='Please fill and select all options before submitting', grid=[1,30])
            pass
        elif [s.find("Duration:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Duration:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,] or [s.find("Duration:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Duration:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1] or [s.find("Duration:") for s in infoList] == [-1, -1, -1, -1, -1, -1, -1, -1, -1]:
            text18 = Text(app, text='Please fill and select all options before submitting', grid=[1,30])
            pass
        else:
            with open('membersdatasaved.txt', 'w') as f:
                for values in infoList:
                    f.write(values + "\n")
            f.close()
            infoList.append('f')
            import sys
            if 'f' in infoList:
                sys.exit()
    submit_button = PushButton(app, text="Submit and Exit", command=text_output_customer_info, grid=[1,29])
    submit_button.bg = but_hex_light

    app.display() 

gym_app()

#////////////DEBUG KIT//////////////////
import os
os.chdir(f'C:/example')
infoList = [
    "Membership Type: Basic $10pw",
    "Duration: 12 Months",
    "Extra(24/7 Access): Yes",
    "Extra(Personal Trainer): Yes",
    "Extra(Diet Consultation): Yes",
    "Extra(Online Fitness Videos): Yes",
    "Direct Debit: Yes",
    "Frequecncy of Payments: Monthly",
]
