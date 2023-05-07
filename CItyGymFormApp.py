#//////////////////////////////////////////////////////////
import pymysql
import os
os.chdir(f'C:/Users/Sam/Documents/OpenPoly/BIT502Ass2')
from guizero import *
global button1, button2, button3, button4, button5, button6, textboxFirst, textboxLast, textboxAddress, textboxNumber, groupButton1, groupButton2, checkBox1, checkBox2, checkBox3, checkBox4, baseMem, durMem, infolist
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

def mem_type_10(infoList, button1):
    '''
     checks if any of the options are already selected, if so the function passes, if not Basic $10pw is added to infoList
    Args:
     infoList, button1
    Returns:
     infoList updated
    '''
    if "Basic $10pw" in infoList:
        pass
    elif "Regular $15pw" in infoList:
        pass
    elif "Premium $20pw" in infoList: 
        pass
    else:
        infoList += [button1.text]
    return(infoList)

def mem_type_15(infoList, button2):
    '''
     checks if any of the options are already selected, if so the function passes, if not Regular $15pw is added to infoList
    Args:
     infoList, button2
    Returns:
     infoList updated
    '''
    if "Basic $10pw" in infoList:
        pass
    elif "Regular $15pw" in infoList:
        pass
    elif "Premium $20pw" in infoList:
        pass
    else:
        infoList += [button2.text]
    return(infoList)

def mem_type_20(infoList, button3):
    '''
     checks if any of the options are already selected, if so the function passes, if not Premium $20pw is added to infoList
    Args:
     infoList, button3
    Returns:
     infoList updated
    '''
    if "Basic $10pw" in infoList:
        pass
    elif "Regular $15pw" in infoList:
        pass
    elif "Premium $20pw" in infoList:
        pass
    else:
        infoList += [button3.text]
    return(infoList)

def mem_dur_3(infoList, button4):
    '''
     checks if any of the options are already selected, if so the function passes, if not 3 Months is added to infoList
    Args:
     infoList, button4
    Returns:
     infoList updated
    '''
    if "3 Months" in infoList:
        pass
    elif "12 Months" in infoList:
        pass
    elif "24 Months" in infoList:
        pass
    else:
        infoList += [button4.text]
    return(infoList)

def mem_dur_12(infoList, button5):
    '''
     checks if any of the options are already selected, if so the function passes, if not 12 Months is added to infoList
    Args:
     infoList, button5
    Returns:
     infoList updated
    '''
    if "3 Months" in infoList:
        pass
    elif "12 Months" in infoList:
        pass
    elif "24 Months" in infoList:
        pass
    else:
        infoList += [button5.text]
    return(infoList)

def mem_dur_24(infoList, button6):
    '''
     checks if any of the options are already selected, if so the function passes, if not 24 Months is added to infoList
    Args:
     infoList, button6
    Returns:
     infoList updated
    '''
    if "3 Months" in infoList:
        pass
    elif "12 Months" in infoList:
        pass
    elif "24 Months" in infoList:
        pass
    else:
        infoList += [button6.text]
    return(infoList)

def direct_credit(infoList, groupButton1):
    '''
     checks if any of the options are already selected, if so the function passes, if not yes or no is added to infoList dependent on switch postion
    Args:
     infoList, groupButton1
    Returns:
     infoList updated
    '''
    if "Yes" in infoList:
        pass
    elif "No" in infoList:
        pass
    else:
        infoList += [groupButton1.value_text]
    return(infoList)

def frq_payment(infoList, groupButton2):
    '''
     checks if any of the options are already selected, if so the function passes, if not Weekly of Monthly is added to infoList
    Args:
     infoList, groupButton2
    Returns:
     infoList updated
    '''
    if "Weekly" in infoList:
        pass
    elif "Monthly" in infoList:
        pass
    else:
        infoList += [groupButton2.value_text]
    return(infoList)

def extras_24(infoList, checkBox1):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts 27/7 
    Args:
     infoList, checkBox1
    Returns:
     infoList updated
    '''
    if checkBox1.value == 1:
        infoList += [checkBox1.text]
    elif checkBox1.value == 0:
        infoList -= [checkBox1.text]
    return(infoList)

def extras_trainer(infoList, checkBox2):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts trainer access to the infoList
    Args:
     infoList, checkBox2
    Returns:
     infoList updated
    '''
    if checkBox2.value == 1:
        infoList += [checkBox2.text]
    elif checkBox2.value == 0:
        infoList -= [checkBox2.text] 
    return(infoList)
        

def extras_diet(infoList, checkBox3):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts diet consultation to the infoList
    Args:
     infoList, checkBox3
    Returns:
     infoList updated
    '''
    if checkBox3.value == 1:
        infoList += [checkBox3.text]
    elif checkBox3.value == 0:
        infoList -= [checkBox3.text]
    return(infoList)

def extras_videos(infoList, checkBox4):
    '''
     checks what the value of the checkbox is 1 or 0 and adds or subtracts video access to the infoList
     none
    Args:
     infoList, checkBox4
    Returns:
     infoList updated
    '''
    if checkBox4.value == 1:
        infoList += [checkBox4.text]
    elif checkBox4.value == 0:
        infoList -= [checkBox4.text] 
    return(infoList)

def calculate_button(infoList):
    '''
     a collection of fuctions to calculate the total payment, lists varibles of options and executes functions
    Args:
     infoList
    Returns:
     the regular payment data
    '''
    basic = 10
    regular = 15
    premium = 20
    access24 = 1
    trainer = 20
    diet = 20
    videos = 2
    perWeek = baseMem + durMem
    regularPay = None
    baseMem = None
    durMem = None

    def base_mem(baseMem):
        '''
         sub-function checks which membership is in the infoList and charges the assocecatied to a varible to be calculated later 
        Args:
         baseMem
        Returns:
         none
        '''
        if "Basic $10pw" in infoList:
            baseMem = basic
        elif "Regular $15pw" in infoList:
            baseMem = regular
        elif "Premium $20pw" in infoList:
            baseMem = premium
        else:
            print('error, restarting app')
            gym_app()

    def dur_mem(durMem):
        '''
         sub-function checks which membership is in the infoList and charges the assocecatied to a varible to be calculated later 
        Args:
         durMem
        Returns:
         none
        '''
        if "3 Months" in infoList:
            pass
        elif "12 Months" in infoList:
            perWeek-2
        elif "24 Months" in infoList:
            perWeek-5
        else:
            print('error, restarting app')
            gym_app()
    
    def extra_mem(perWeek, checkBox1, checkBox2, checkBox3, checkBox4):
        '''
         sub-function checks which of the extra options if any are in infoList and adds the asscoitated options varible to the total  
        Args:
         perWeek, checkBox1, checkBox2, checkBox3, checkBox4
        Returns:
         none
        '''
        if [checkBox1.text] in infoList:
            perWeek += access24
        elif [checkBox2.text] in infoList:
            perWeek += trainer
        elif [checkBox3.text] in infoList:
            perWeek += diet
        elif [checkBox4.text] in infoList:
            perWeek += videos

    def pay_mem(baseMem):
        '''
         sub-function checks if either yes or no for direct payment and subtracts a 1% discount from total
        Args:
         baseMem 
        Returns:
         none
        '''
        if "Yes" in infoList:
            discount = 1 * baseMem/100
            baseMem - discount
        elif "No" in infoList:
            pass

    def frq_mem(perWeek, regularPay, infoList):
        '''
         sub-function checks if either weekly or monthly are selected from the infoList and adjusts the regular payment
        Args:
         perWeek,regularPay,infoList
        Returns:
         none
        '''
        if "Weekly" in infoList:
            regularPay = perWeek
            infoList += regularPay
        elif "Monthly" in infoList:
            regularPay = perWeek * 4
            infoList += regularPay

    base_mem()
    dur_mem()
    extra_mem(perWeek, checkBox1, checkBox2, checkBox3, checkBox4, infoList)
    pay_mem(baseMem, infoList)
    frq_mem(perWeek, regularPay, infoList)
    return(regularPay)

def text_output_customer_info(infoList):
    '''
     outputs the new client infolist as a text file
    Args:
     infoList
    Returns:
     none
    '''
    with open(f'C:/example/readme.txt', 'w') as f:
        for info in infoList:
            f.write(info)

def send_customer_info(infoList):
    '''
    Example mysql query, would be used to update a DB with customer info
    
    '''
    conn = pymysql.connect(host= "server",
                       user="user",
                       passwd="pw",
                       db="db",
                       charset='utf8')
    query = "UPDATE new_customer SET first_name= '{infoList[0]}', last_name='{infoList[1]}', Address='{infoList[2]}' WHERE displayName='{infoList[3]}'"
    conn.ping()
    x = conn.cursor()
    x.execute(query)

#/////////////////////////////////////////////////////
#Header title
def gym_app(infoList):
    '''
     main guizero code block, sets up placement of assests in the frame and intergration of customer fucntions
    Args:
     none
    Returns:
     an interactive gui
    
    '''
    app = App(title="City Gym", height=1200, width=500, layout="auto")
    picture = Picture(app, image="citygymlogo.png", grid=[1,0])
    text = Text(app, text="City Gym", grid=[1,1])
    text = Text(app, text="Membership Form", grid=[1,2])
#//////////////////////////////////////////////////////
#Customer inputs
    text = Text(app, text="", grid=[1,3])
    text = Text(app, text="CUSTOMER DETAILS", grid=[1,4])
    textboxFirst = TextBox(app, text="First name", grid=[1,5], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,6], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,7], width=20)
    textboxNumber =TextBox(app, text="Mobile number", grid=[1,8], width=20)
    infoList = [textboxFirst.value], 
    [textboxLast.value], 
    [textboxAddress.value],  
    [textboxNumber.value],
#///////////////////////////////////////////////////
#Memebership buttons
    def discount_note_seen():
        text = Text(app, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,13], visible=True)
    def discount_note_hide():
        text = Text(app, text="Sign up for a 12-month contract to receive a $2 per week discount on any membership type.\nSign up for 24 months to receive a $5 per week discount on any membership type.", grid=[1,13], visible=False)
    text = Text(app, text="", grid=[1,9])
    text = Text(app, text="MEMBERSHIP DETAILS", grid=[1,10])
    text = Text(app, text="Membership Type", grid=[1,11])
    but_hex = "#7B61FF"
    box = Box(app, layout="grid", grid=[1,12])
    button1 = PushButton(box, text="Basic $10pw", command=mem_type_10(infoList, button1), grid=[0,1])
    button2 = PushButton(box, text="Regular $15pw", command=mem_type_15(infoList, button2), grid=[1,1])
    button3 = PushButton(box, text="Premium $20pw", command=mem_type_20(infoList, button3), grid=[2,1])
    button1.bg = but_hex
    button2.bg = but_hex
    button3.bg = but_hex
    text = Text(app, text="Membership Duration", grid=[1,13])
    box1 = Box(app, layout="grid", grid=[1,14])
    button4 = PushButton(box1, text="3 Months", command=mem_dur_3(infoList, button4), grid=[0,1])
    button4.when_mouse_enters = discount_note_seen()
    button4.when_mouse_leaves = discount_note_hide()
    button5 = PushButton(box1, text="12 Months", command=mem_dur_12(infoList, button5),grid=[1,1])
    button5.when_mouse_enters = discount_note_seen()
    button5.when_mouse_leaves = discount_note_hide()
    button6 = PushButton(box1, text="24 Months", command=mem_dur_24(infoList, button6),grid=[2,1])
    button6.when_mouse_enters = discount_note_seen()
    button6.when_mouse_leaves = discount_note_hide()
    button4.bg = but_hex
    button5.bg = but_hex
    button6.bg = but_hex
#///////////////////////////////////////////////////////////
#Payment options
    def discount_payment_seen():
        text = Text(app, text="For direct debits, there is a 1% discount on the base membership cost.", grid=[1,17], visible=True)
    def discount_payment_hide():
        text = Text(app, text="For direct debits, there is a 1% discount on the base membership cost.", grid=[1,17], visible=False)
    text = Text(app, text="", grid=[1,15])
    text = Text(app, text="PAYMENT OPTIONS", grid=[1,16])
    text = Text(app, text="Direct Debt", grid=[1,17])
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected="Yes", command=direct_credit(infoList, groupButton1), grid=[1,18])
    groupButton1.when_mouse_enters = discount_payment_seen()
    groupButton1.when_mouse_leaves = discount_payment_hide()
    text = Text(app, text="Frequecncy of payments", grid=[1,19])
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected="Weekly", command=frq_payment(infoList, groupButton2), grid=[1,20])
#///////////////////////////////////////////////////////////
#Extras
    text = Text(app, text="", grid=[1,21])
    text = Text(app, text="EXTRAS", grid=[1,22])
    text = Text(app, )
    checkBox1 = CheckBox(app, text="24/7 Access/$1pw", command=extras_24(infoList, checkBox1), grid=[1,23])
    checkBox2 = CheckBox(app, text="Personal Trainer/$20pw", command=extras_trainer(infoList, checkBox2), grid=[1,24])
    checkBox3 = CheckBox(app, text="Diet Consultation/$20pw", command=extras_diet(infoList, checkBox3), grid=[1,25])
    checkBox4 = CheckBox(app, text="Online Fitness Videos/$2pw", command=extras_videos(infoList, checkBox4), grid=[1,26])
    text = Text(app, text="", grid=[1,27])
    text = Text(app, text="PAYMENT TOTAL", grid=[1,26])
    text = Text(app, text="", grid=[1,28])
    listbox = ListBox(app, items=['place holder'], grid=[1,29])
    cal_button = PushButton(app, text="Calculate Membership", command=calculate_button(infoList), grid=[1,30])
    download_button = PushButton(app, text="Download details", command=text_output_customer_info(infoList), grid=[1,31])
    exit_button = PushButton(app, text="Submit and Exit", command=exit_citygym(), grid=[1,32])
#///////////////////////////////////////////////////////////
#Start
    app.display() 
    app.mainloop()
gym_app(infoList)
send_customer_info(infoList)
