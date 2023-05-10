#//////////////////////////////////////////////////////////
import pymysql
import os
os.chdir(f'C:/Users/eastt/OneDrive/Documents/OpenPoly/502')
from guizero import *
global button1, button2, button3, button4, button5, button6, textboxFirst, textboxLast, textboxAddress, textboxNumber, groupButton1, groupButton2, checkBox1, checkBox2, checkBox3, checkBox4, infolist
infoList = []
#//////////////////////////////////////////////////
#Custom Functions
def exit_citygym():
    '''
     a simple sys based fucntion to exit the app
    Args:
     none   
    Returns:
     none
    '''
    import sys
    sys.exit()

def mem_type_10():
    '''
    checks if any of the options are already selected, if so the function passes, if not Basic $10pw is added to infoList
    Args:
    infoList
    Returns:
    infoList updated
    '''
    if "Membership Type: Basic $10pw" in infoList[:]:
        pass
    elif "Membership Type: Regular $15pw" in infoList[:]:
        pass
    elif "Membership Type: Premium $20pw" in infoList[:]: 
        pass
    else:
        infoList.append("Membership Type: Basic $10pw")
    return(infoList)

def mem_type_15():
    '''
     checks if any of the options are already selected, if so the function passes, if not Regular $15pw is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Membership Type: Basic $10pw" in infoList:
        pass
    elif "Membership Type: Regular $15pw" in infoList:
        pass
    elif "Membership Type: Premium $20pw" in infoList: 
        pass
    else:
        infoList.append("Membership Type: Regular $15pw")
    return(infoList)

def mem_type_20():
    '''
     checks if any of the options are already selected, if so the function passes, if not Premium $20pw is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Membership Type: Basic $10pw" in infoList:
        pass
    elif "Membership Type: Regular $15pw" in infoList:
        pass
    elif "Membership Type: Premium $20pw" in infoList: 
        pass
    else:
        infoList.append("Membership Type: Regular $20pw")
    return(infoList)

def mem_dur_3():
    '''
     checks if any of the options are already selected, if so the function passes, if not 3 Months is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Duration: 3 Months" in infoList:
        pass
    elif "Duration: 12 Months" in infoList:
        pass
    elif "Duration: 24 Months" in infoList: 
        pass
    else:
        infoList.append("Duration: 3 Months")
    return(infoList)

def mem_dur_12():
    '''
     checks if any of the options are already selected, if so the function passes, if not 12 Months is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Duration: 3 Months" in infoList:
        pass
    elif "Duration: 12 Months" in infoList:
        pass
    elif "Duration: 24 Months" in infoList: 
        pass
    else:
        infoList.append("Duration: 12 Months")
    return(infoList)

def mem_dur_24():
    '''
     checks if any of the options are already selected, if so the function passes, if not 24 Months is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Duration: 3 Months" in infoList:
        pass
    elif "Duration: 12 Months" in infoList:
        pass
    elif "Duration: 24 Months" in infoList: 
        pass
    else:
        infoList.append("Duration: 24 Months")
    return(infoList)

def direct_credit(groupButton1):
    '''
     checks if any of the options are already selected, if so the function passes, if not yes or no is added to infoList dependent on switch postion
    Args:
     infoList
    Returns:
     infoList updated
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

def frq_payment(groupButton2):
    '''
     checks if any of the options are already selected, if so the function passes, if not Weekly of Monthly is added to infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Frequecncy of Payments: Weekly" in infoList:
        pass
    elif "Frequecncy of Payments: Monthly" in infoList:
        pass
    else:
        if groupButton2.value == 1:
            infoList.append("Frequecncy of Payments: Weekly")
        elif groupButton2.value == 0:
            infoList.append("Frequecncy of Payments: Weekly")
    return(infoList)

def extras_24(checkBox1):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts 27/7 
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Extra(24/7 Access): Yes" in infoList:
        pass
    elif "Extra(24/7 Access): No" in infoList:
        pass
    else:
        if checkBox1.value == 1:
            infoList.append('Extra(24/7 Access): Yes')
        elif checkBox1.value == 0:
            infoList.append("Extra(24/7 Access): No")
    return(infoList)

def extras_trainer(checkBox2):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts trainer access to the infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Extra(Personal Trainer): Yes" in infoList:
        pass
    elif "Extra(Personal Trainer): No" in infoList:
        pass
    else:
        if checkBox2.value == 1:
            infoList.append("Extra(Personal Trainer): Yes")
        elif checkBox2.value == 0:
            infoList.append("Extra(Personal Trainer): No")
    return(infoList)

def extras_diet(checkBox3):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts diet consultation to the infoList
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Extra(Diet Consultation): Yes" in infoList:
        pass
    elif "Extra(Diet Consultation): No" in infoList:
        pass
    else:
        if checkBox3.value == 1:
            infoList.append("Extra(Diet Consultation): Yes")
        elif checkBox3.value == 0:
            infoList.append("Extra(Diet Consultation): No")
    return(infoList)

def extras_videos(checkBox4):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts video access to the infoList
     none
    Args:
     infoList
    Returns:
     infoList updated
    '''
    if "Extra(Online Fitness Videos): Yes" in infoList:
        pass
    elif "Extra(Online Fitness Videos): No" in infoList:
        pass
    else:
        if checkBox4.value == 1:
            infoList.append("Extra(Online Fitness Videos): Yes")
        elif checkBox4.value == 0:
            infoList.append("Extra(Online Fitness Videos): No")
    return(infoList)

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
        if "Membership Type: Basic $10pw" in infoList:
            baseMem = 10
        elif "Membership Type: Regular $15pw" in infoList:
            baseMem = 15
        elif "Membership Type: Premium $20pw" in infoList:
            baseMem = 20
        else:
            print('error, restarting app')
        return(baseMem)


    def dur_mem():
        '''
         sub-function checks which membership is in the infoList and charges the assocecatied to a varible to be calculated later 
        Args:
         durMem, infoList
        Returns:
         none
        '''
        global durMem
        if "Duration: 3 Months" in infoList:
            durMem = 0
        elif "Duration: 12 Months" in infoList:
            durMem = -2
        elif "Duration: 24 Months" in infoList:
            durMem = -5
        else:
            print('error, restarting app')
        return(durMem)

    
    def extra_mem(perWeek):
        '''
         sub-function checks which of the extra options if any are in infoList and adds the asscoitated options varible to the total  
        Args:
         perWeek, infoList
        Returns:
         none
        '''
        if "Extra(24/7 Access): Yes" in infoList:
            perWeek + 1
        elif "Extra(Personal Trainer): Yes" in infoList:
            perWeek + 20
        elif "Extra(Diet Consultation): Yes" in infoList:
            perWeek + 20
        elif "Extra(Online Fitness Videos): Yes" in infoList:
            perWeek + 2
        return(perWeek)

    def pay_mem(baseMem1):
        '''
         sub-function checks if either yes or no for direct payment and subtracts a 1% discount from total
        Args:
         baseMem, infoList
        Returns:
         none
        '''
        if "Direct Debit: Yes" in infoList:
            discount = 1 * baseMem/100
            baseMem2 = baseMem1 - discount
            baseMem1 = baseMem2
        elif "Direct Debit: No" in infoList:
            pass
        return(baseMem1)

    def frq_mem(perWeek):
        '''
         sub-function checks if either weekly or monthly are selected from the infoList and adjusts the regular payment
        Args:
         perWeek,regularPay,infoList
        Returns:
         none
        '''
        global regularPay
        if "Frequecncy of Payments: Weekly" in infoList:
            regularPay = perWeek
            infoList.update({13:"Regular Payments: " + str(regularPay)})
        elif "Frequecncy of Payments: Weekly" in infoList:
            regularPay = perWeek * 4
            infoList.update({13:"Regular Payments: " + str(regularPay)})

    baseMem1 = base_mem()
    durMem1 = dur_mem()
    baseMem3 = pay_mem(baseMem1)
    perWeek = baseMem3 + durMem1
    extra_mem(perWeek)
    frq_mem(perWeek)

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

def send_customer_info():
    '''
    Example mysql query, would be used to update a DB with customer info
    
    '''
    conn = pymysql.connect(host= "server",
                       user="user",
                       passwd="pw",
                       db="db",
                       charset='utf8')
    query = "UPDATE new_customer SET first_name= '{infoList[1]}', last_name='{infoList[2]}', Address='{infoList[3]}' WHERE displayName='{infoList[4]}'"
    conn.ping()
    x = conn.cursor()
    x.execute(query)

#/////////////////////////////////////////////////////
#Header title
def gym_app():
    '''
     main guizero code block, sets up placement of assests in the frame and intergration of customer fucntions
    Args:
     none
    Returns:
     an interactive gui
    
    '''
    app = App(title="City Gym", height=1200, width=800, layout="auto")
    picture = Picture(app, image="citygymlogo.png", grid=[1,0])
    text1 = Text(app, text="City Gym", grid=[1,1])
    text2 = Text(app, text="Membership Form", grid=[1,2])
    text3 = Text(app, text="", grid=[1,3])
    text4 = Text(app, text="CUSTOMER DETAILS", grid=[1,4])
    textboxFirst = TextBox(app, text="First name", grid=[1,5], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,6], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,7], width=20)
    textboxNumber =TextBox(app, text="Mobile number", grid=[1,8], width=20)
    infoList = ["First Name: " + str(textboxFirst.value), 
    "Last Name: " + str(textboxLast.value), 
    "Address: " + str(textboxAddress.value),  
    "Mobile Number: " + str(textboxNumber.value)]
    text5 = Text(app, text="", grid=[1,9])
    text6 = Text(app, text="MEMBERSHIP DETAILS", grid=[1,10])
    text7 = Text(app, text="Membership Type", grid=[1,11])
    but_hex = "#7B61FF"
    box = Box(app, layout="grid", grid=[1,12])
    button1 = PushButton(box, text="Basic $10pw", grid=[0,1])
    button1.when_clicked = mem_type_10()
    button2 = PushButton(box, text="Regular $15pw", grid=[1,1])
    button2.when_clicked = mem_type_15()
    button3 = PushButton(box, text="Premium $20pw", grid=[2,1])
    button3.when_clicked = mem_type_20()
    button1.bg = but_hex
    button2.bg = but_hex
    button3.bg = but_hex
    text8 = Text(app, text="Membership Duration", grid=[1,13])
    box1 = Box(app, layout="grid", grid=[1,14])
    button4 = PushButton(box1, text="3 Months", grid=[0,1])
    button4.when_clicked = mem_dur_3()
    button5 = PushButton(box1, text="12 Months", command=mem_dur_12(),grid=[1,1])
    button5.when_clicked = mem_dur_12
    button6 = PushButton(box1, text="24 Months", command=mem_dur_24(),grid=[2,1])
    button4.bg = but_hex
    button5.bg = but_hex
    button6.bg = but_hex
    text9 = Text(app, color=but_hex, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,15])
    text10 = Text(app, text="", grid=[1,15])
    text11 = Text(app, text="PAYMENT OPTIONS", grid=[1,16])
    text12 = Text(app, text="Direct Debt", grid=[1,17])
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected="Yes", grid=[1,18])
    groupButton1.when_clicked = direct_credit(groupButton1)
    text13 = Text(app, text="Frequecncy of payments", grid=[1,19])
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected="Weekly", grid=[1,20])
    groupButton2.when_clicked = frq_payment(groupButton2)
    text14 = Text(app, text="", grid=[1,21])
    text15 = Text(app, text="EXTRAS", grid=[1,22])
    checkBox1 = CheckBox(app, text="24/7 Access/$1pw", grid=[1,23])
    checkBox1.when_clicked = extras_24(checkBox1)
    checkBox2 = CheckBox(app, text="Personal Trainer/$20pw", grid=[1,24])
    checkBox2.when_clicked = extras_trainer(checkBox2)
    checkBox3 = CheckBox(app, text="Diet Consultation/$20pw", grid=[1,25])
    checkBox3.when_clicked = extras_diet(checkBox3),
    checkBox4 = CheckBox(app, text="Online Fitness Videos/$2pw", grid=[1,26])
    checkBox4.when_clicked = extras_videos(checkBox4)
    text16 = Text(app, text="", grid=[1,27])
    text17 = Text(app, text="PAYMENT TOTAL", grid=[1,26])
    text18 = Text(app, text="", grid=[1,28])
    listbox = ListBox(app, items=['place holder'], grid=[1,29])
    cal_button = PushButton(app, text="Calculate Membership", grid=[1,30])
    cal_button.when_clicked = calculate_button()
    download_button = PushButton(app, text="Download details", grid=[1,31])
    download_button.when_clicked = text_output_customer_info()
    exit_button = PushButton(app, text="Submit and Exit", grid=[1,32])
    #exit_button.when_clicked = exit_citygym()
    app.display() 

gym_app(infoList)
send_customer_info(infoList)
