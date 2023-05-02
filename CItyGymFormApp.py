#//////////////////////////////////////////////////////////
import pymysql
from guizero import *
#//////////////////////////////////////////////////
#Custom Functions
def exit_citygym():
    '''
    placeholdedr
    '''
    import sys
    sys.exit()

def mem_type_10():
    '''
    placeholdedr
    '''
    if "Basic $10pw" in infolist:
        pass
    elif "Regular $15pw" in infolist:
        pass
    elif "Premium $20pw" in infolist:
        pass
    else:
        infoList += [button1.text]

def mem_type_15():
    '''
    placeholdedr
    '''
    if "Basic $10pw" in infolist:
        pass
    elif "Regular $15pw" in infolist:
        pass
    elif "Premium $20pw" in infolist:
        pass
    else:
        infoList += [button2.text]

def mem_type_20():
    '''
    placeholdedr
    '''
    if "Basic $10pw" in infolist:
        pass
    elif "Regular $15pw" in infolist:
        pass
    elif "Premium $20pw" in infolist:
        pass
    else:
        infoList += [button3.text]

def mem_dur_3():
    '''
    placeholdedr
    '''
    if "3 Months" in infolist:
        pass
    elif "12 Months" in infolist:
        pass
    elif "24 Months" in infolist:
        pass
    else:
        infoList += [button4.text]

def mem_dur_12():
    '''
    placeholdedr
    '''
    if "3 Months" in infolist:
        pass
    elif "12 Months" in infolist:
        pass
    elif "24 Months" in infolist:
        pass
    else:
        infoList += [button5.text]

def mem_dur_24():
    '''
    placeholdedr
    '''
    if "3 Months" in infolist:
        pass
    elif "12 Months" in infolist:
        pass
    elif "24 Months" in infolist:
        pass
    else:
        infoList += [button6.text]

def direct_credit():
    '''
    placeholdedr
    '''
    if "Yes" in infolist:
        pass
    elif "No" in infolist:
        pass
    else:
        infolist += [groupButton1.value_text]

def frq_payment():
    '''
    placeholdedr
    '''
    if "Weekly" in infolist:
        pass
    elif "Monthly" in infolist:
        pass
    else:
        infolist += [groupButton2.value_text]

def extras_24():
    '''
    placeholdedr
    '''
    if checkBox1.value == 1:
        infoList += [checkBox1.text]
    elif checkBox1.value == 0:
        infolist -= [checkBox1.text]

def extras_trainer():
    '''
    placeholdedr
    '''
    if checkBox2.value == 1:
        infoList += [checkBox2.text]
    elif checkBox2.value == 0:
        infolist -= [checkBox2.text] 

def extras_diet():
    '''
    placeholdedr
    '''
    if checkBox3.value == 1:
        infoList += [checkBox3.text]
    elif checkBox3.value == 0:
        infolist -= [checkBox3.text] 

def extras_videos():
    '''
    placeholdedr
    '''
    if checkBox4.value == 1:
        infoList += [checkBox4.text]
    elif checkBox4.value == 0:
        infolist -= [checkBox4.text] 

def send_customer_info():
    '''
    Example mysql query, for demonstrative purposes only
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
def gym_app():
    '''
    comment
    '''
    app = App(title="City Gym", height=1200, width=500, layout="auto")
    picture = Picture(app, image="citygymlogo.png", grid=[1,0])
    text = Text(app, text="City Gym", grid=[1,1])
    text = Text(app, text="Membership Form", grid=[1,2])
    global infolist
    infolist = [textboxFirst.value], 
    [textboxLast.value], 
    [textboxAddress.value], 
    [textboxNumber.value],
#//////////////////////////////////////////////////////
#Customer inputs
    text = Text(app, text="", grid=[1,3])
    text = Text(app, text="CUSTOMER DETAILS", grid=[1,4])
    global textboxFirst, textboxLast, textboxAddress, textboxNumber
    textboxFirst = TextBox(app, text="First name", grid=[1,5], width=20)
    textboxLast = TextBox(app, text="Last name", grid=[1,6], width=20)
    textboxAddress = TextBox(app, text="Address", grid=[1,7], width=20)
    textboxNumber =TextBox(app, text="Mobile number", grid=[1,8], width=20)
#///////////////////////////////////////////////////
#Memebership buttons
    text = Text(app, text="", grid=[1,9])
    text = Text(app, text="MEMBERSHIP DETAILS", grid=[1,10])
    text = Text(app, text="Membership Type", grid=[1,11])
    but_hex = "#7B61FF"
    box = Box(app, layout="grid", grid=[1,12])
    global button1, button2, button3, button4, button5, button6
    button1 = PushButton(box, text="Basic $10pw", command=mem_type_10, grid=[0,1])
    button2 = PushButton(box, text="Regular $15pw", command=mem_type_15, grid=[1,1])
    button3 = PushButton(box, text="Premium $20pw", command=mem_type_20, grid=[2,1])
    button1.bg = but_hex
    button2.bg = but_hex
    button3.bg = but_hex
    text = Text(app, text="Membership Duration", grid=[1,13])
    box1 = Box(app, layout="grid", grid=[1,14])
    button4 = PushButton(box1, text="3 Months", command=mem_dur_3(), grid=[0,1])
    button5 = PushButton(box1, text="12 Months", command=mem_dur_12(),grid=[1,1])
    button6 = PushButton(box1, text="24 Months", command=mem_dur_24(),grid=[2,1])
    button4.bg = but_hex
    button5.bg = but_hex
    button6.bg = but_hex
#///////////////////////////////////////////////////////////
#Payment options
    text = Text(app, text="", grid=[1,15])
    text = Text(app, text="PAYMENT OPTIONS", grid=[1,16])
    text = Text(app, text="Direct Debt", grid=[1,17])
    global groupButton1, groupButton2
    groupButton1 = ButtonGroup(app, options=["Yes", "No"], selected="Yes", command=direct_credit(), grid=[1,18])
    text = Text(app, text="Frequecncy of payments", grid=[1,19])
    groupButton2 = ButtonGroup(app, options=["Weekly", "Monthly"], selected="Weekly", command=frq_payment(), grid=[1,20])
#///////////////////////////////////////////////////////////
#Extras
    text = Text(app, text="", grid=[1,21])
    text = Text(app, text="EXTRAS", grid=[1,22])
    global checkBox1, checkBox2, checkBox3, checkBox4
    checkBox1 = CheckBox(app, text="24/7 Access/$1pw", command=extras_24(), grid=[1,23])
    checkBox2 = CheckBox(app, text="Personal Trainer/$20pw", command=extras_trainer(), grid=[1,24])
    checkBox3 = CheckBox(app, text="Diet Consultation/$20pw", command=extras_diet(), grid=[1,25])
    checkBox4 = CheckBox(app, text="Online Fitness Videos/$2pw", command=extras_videos(), grid=[1,26])
    text = Text(app, text="", grid=[1,27])
    text = Text(app, text="PAYMENT TOTAL", grid=[1,26])
    text = Text(app, text="", grid=[1,27])
    listbox = ListBox(app, items=['place holder'], grid=[1,28])
    cal_button = PushButton(app, text="Calculate Membership", grid=[1,29])
    exit_button = PushButton(app, text="Submit and Exit", command=send_customer_info(), command=exit_citygym, grid=[1,30])
#///////////////////////////////////////////////////////////
#Start
    app.display()
