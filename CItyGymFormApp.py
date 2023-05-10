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
    infoList = ["Customer Sign-up Info",]
    but_hex = "#7B61FF"
    but_hex_light = "#c5b9ff"

    app = App(title="City Gym", height=1200, width=700, layout="auto")

    picture = Picture(app, image="citygymlogo.png", grid=[1,0])

    text1 = Text(app, text="City Gym", grid=[1,1])
    text2 = Text(app, text="Membership Form", grid=[1,2])
    text3 = Text(app, text="", grid=[1,3])
    text4 = Text(app, text="CUSTOMER DETAILS", grid=[1,4])
    global textboxFirst, textboxLast, textboxAddress, textboxNumber
    textboxFirst = TextBox(app, text="First name", grid=[1,5], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,6], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,7], width=20)
    textboxNumber = TextBox(app, text="Mobile number", grid=[1,8], width=20)

    global button
    button = PushButton(app, text="Enter", grid=[1,9])
    button.bg = but_hex
    def personal_info():
        '''
         widget function: checks if personal info has been added to the infoList or if defaults are still in field
         if not the new completed fields are added to infoList
        '''
        if "Personal Info" in infoList:
            pass
        elif "First name" in infoList:
            pass
        elif "Last name" in infoList:
            pass
        elif "Address" in infoList:
            pass
        elif "Mobile number" in infoList:
            pass
        else:
            infoList.extend([
            "Personal Info",
            "First Name: " + str(textboxFirst.value), 
            "Last Name: " + str(textboxLast.value),
            "Address: " + str(textboxAddress.value),
            "Mobile Number: " + str(textboxNumber.value),
            ])     
        button.hide
        thxText = Text(app, text="Thank you!", grid=[1,9])
    button.when_clicked = personal_info()

    text5 = Text(app, text="", grid=[1,10])
    text6 = Text(app, text="MEMBERSHIP DETAILS", grid=[1,11])
    text7 = Text(app, text="Membership Type", grid=[1,12])

    box = Box(app, layout="grid", grid=[1,13])

    global button1
    button1 = PushButton(box, text="Basic $10pw", grid=[0,1])
    button1.bg = but_hex
    def mem_type_10():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not basic membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            pass
        elif "Membership Type: Regular $15pw" in infoList:
            pass
        elif "Membership Type: Premium $20pw" in infoList: 
            pass
        else:
            infoList.append("Membership Type: Basic $10pw")
    button1.when_clicked = mem_type_10()

    global button2
    button2 = PushButton(box, text="Regular $15pw", grid=[1,1])
    button2.bg = but_hex
    def mem_type_15():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not regular membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            pass
        elif "Membership Type: Regular $15pw" in infoList:
            pass
        elif "Membership Type: Premium $20pw" in infoList: 
            pass
        else:
            infoList.append("Membership Type: Regular $15pw")
    button2.when_clicked = mem_type_15()

    global button3
    button3 = PushButton(box, text="Premium $20pw", grid=[2,1])
    button3.bg = but_hex
    def mem_type_20():
        '''
         widget function: checks if a membership type has been added to the infoList
         if not premium membership is added to infoList
        '''
        if "Membership Type: Basic $10pw" in infoList:
            pass
        elif "Membership Type: Regular $15pw" in infoList:
            pass
        elif "Membership Type: Premium $20pw" in infoList: 
            pass
        else:
            infoList.append("Membership Type: Premium $20pw")
    button3.when_clicked = mem_type_20()
    
    text8 = Text(app, text="Membership Duration", grid=[1,14])
    
    box1 = Box(app, layout="grid", grid=[1,15])

    global button4
    button4 = PushButton(box1, text="3 Months", grid=[0,1])
    button4.bg = but_hex
    def mem_dur_3():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 3 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            pass
        elif "Duration: 12 Months" in infoList:
            pass
        elif "Duration: 24 Months" in infoList: 
            pass
        else:
            infoList.append("Duration: 3 Months")
    button4.when_clicked = mem_dur_3()

    global button5
    button5 = PushButton(box1, text="12 Months", grid=[1,1])
    button5.bg = but_hex
    def mem_dur_12():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 12 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            pass
        elif "Duration: 12 Months" in infoList:
            pass
        elif "Duration: 24 Months" in infoList: 
            pass
        else:
            infoList.append("Duration: 12 Months")
    button5.when_clicked = mem_dur_12()

    global button6
    button6 = PushButton(box1, text="24 Months", grid=[2,1])
    button6.bg = but_hex
    def mem_dur_24():
        '''
         widget function: checks if a membership duration has been added to the infoList
         if not 24 months is added to infoList
        '''
        if "Duration: 3 Months" in infoList:
            pass
        elif "Duration: 12 Months" in infoList:
            pass
        elif "Duration: 24 Months" in infoList: 
            pass
        else:
            infoList.append("Duration: 24 Months")
    button6.when_clicked = mem_dur_24()  

    text9 = Text(app, color=but_hex, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,15])
    text10 = Text(app, text="", grid=[1,16])

    text11 = Text(app, text="PAYMENT OPTIONS", grid=[1,17])
    text12 = Text(app, text="Direct Debt", grid=[1,18])

    global groupButton1
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected=None, grid=[1,19])
    groupButton1.bg = but_hex_light
    def direct_credit():
        '''
         widget function: checks if payment option has been added to the infoList
         if not a check on which postion the buttongroup is on and adds the selection to infoList
        '''
        if "Direct Debit: Yes" in infoList:
            pass
        elif "Direct Debit: No" in infoList:
            pass
        else:
            if groupButton1.value == 1:
                infoList.append("Direct Debit: Yes")
            elif groupButton1.value == 0:
                infoList.append("Direct Debit: No")
    groupButton1.when_clicked = direct_credit()

    text13 = Text(app, text="Frequecncy of payments", grid=[1,20])

    global groupButton2
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected=None, grid=[1,21])
    groupButton2.bg = but_hex_light
    def frq_payment():
        '''
         widget function: checks if payment freq option has been added to the infoList
         if not a check on which postion the buttongroup is on and adds the selection to infoList
        '''
        if "Frequecncy of Payments: Weekly" in infoList:
            pass
        elif "Frequecncy of Payments: Monthly" in infoList:
            pass
        else:
            if groupButton2.value == 1:
                infoList.append("Frequecncy of Payments: Weekly")
            elif groupButton2.value == 0:
                infoList.append("Frequecncy of Payments: Monthly")
    groupButton2.when_clicked = frq_payment()

    text14 = Text(app, text="", grid=[1,22])

    text15 = Text(app, text="EXTRAS", grid=[1,23])

    global checkBox1
    checkBox1 = CheckBox(app, text="24/7 Access/$1pw", grid=[1,24])
    checkBox1.bg = but_hex_light
    def extra_24():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            pass
        elif "Extra(24/7 Access): No" in infoList:
            pass
        else:
            if checkBox1.value == 1:
                infoList.append("Extra(24/7 Access): Yes")
            elif checkBox1.value == 0:
                infoList.append("Extra(24/7 Access): No")
    checkBox1.when_clicked = extra_24()

    global checkBox2
    checkBox2 = CheckBox(app, text="Personal Trainer/$20pw", grid=[1,25])
    checkBox2.bg = but_hex_light
    def extra_trainer():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            pass
        elif "Extra(24/7 Access): No" in infoList:
            pass
        else:
            if checkBox1.value == 1:
                infoList.append("Extra(24/7 Access): Yes")
            elif checkBox1.value == 0:
                infoList.append("Extra(24/7 Access): No")
    checkBox2.when_clicked = extra_trainer()

    global checkBox3
    checkBox3 = CheckBox(app, text="Diet Consultation/$20pw", grid=[1,26])
    checkBox3.bg = but_hex_light
    def extra_diet():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            pass
        elif "Extra(24/7 Access): No" in infoList:
            pass
        else:
            if checkBox1.value == 1:
                infoList.append("Extra(24/7 Access): Yes")
            elif checkBox1.value == 0:
                infoList.append("Extra(24/7 Access): No")
    checkBox3.when_clicked = extra_diet()

    global checkBox4
    checkBox4 = CheckBox(app, text="Online Fitness Videos/$2pw", grid=[1,27])
    checkBox4.bg = but_hex_light
    def extra_video():
        '''
         widget function: checks if the extra option has been added to the infoList
         if not a check on which postion the checkbox is on and adds the selection to infoList
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            pass
        elif "Extra(24/7 Access): No" in infoList:
            pass
        else:
            if checkBox1.value == 1:
                infoList.append("Extra(24/7 Access): Yes")
            elif checkBox1.value == 0:
                infoList.append("Extra(24/7 Access): No")
    checkBox4.when_clicked = extra_video()

    text16 = Text(app, text="", grid=[1,28])
    text17 = Text(app, text="PAYMENT TOTAL", grid=[1,29])
    text18 = Text(app, text="", grid=[1,30])

    listBox = ListBox(app, items=[
    {infoList[0]},
    {infoList[1]},
    {infoList[2]},
    {infoList[3]},
    {infoList[4]},
    {infoList[5]},
    {infoList[6]},
    {infoList[7]},
    {infoList[8]},
    {infoList[9]},
    {infoList[10]},
    {infoList[11]},
    ], grid=[1,31])
    listBox.bg = but_hex_light

    cal_button = PushButton(app, text="Calculate Membership", grid=[1,32])
    cal_button.bg = but_hex
    def calculate_button(infoList):
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
                regularPay = perWeek
            elif "Frequecncy of Payments: Monthly" in infoList:
                regularPay = perWeek * 4
            return(regularPay)

        global baseMem, durMem, disMem
        base_mem()
        dur_mem()
        pay_mem()
        global perWeek
        perWeek = (baseMem - disMem) + durMem
        #//////////////START FROM HER///////////////
        extra_mem(perWeek)
        global regularPay1
        regularPay1 = frq_mem(exPerWeek)  
    cal_button.when_clicked = calculate_button(infoList)

    download_button = PushButton(app, text="Download details", grid=[1,33])
    download_button.bg = but_hex_light
    def text_output_customer_info():
        '''
         outputs the new client infolist as a text file
        Args:
         infoList
        Returns:
         none
        '''
        with open('CityGymOutput.txt', 'w') as f:
            for values in infoList:
                f.write("\n" + values)
        f.close()
    download_button.when_clicked = text_output_customer_info()

    exit_button = PushButton(app, text="Submit and Exit", grid=[1,34])
    exit_button.bg = but_hex_light
    def send_customer_info():
        '''
         example mysql query, would be used to update a DB with customer info
         sends new client infomation to sql server and exits the app
        '''
        import pymysql
        conn = pymysql.connect(host= "server",
                        user="user",
                        passwd="pw",
                        db="db",
                        charset='utf8')
        query = "UPDATE new_customer SET first_name= '{infoList[0]}', last_name='{infoList[1]}', Address='{infoList[2]}' WHERE displayName='{infoList[3]}'"
        conn.ping()
        x = conn.cursor()
        x.execute(query)
        import sys
        sys.exit()

    exit_button.when_clicked = send_customer_info()
    exit_button.when_clicked = exit_citygym()

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
