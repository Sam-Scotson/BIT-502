#//////////////////////////////////////////////////////////
from guizero import App, Window, Text, Box, CheckBox, ListBox, PushButton, Picture, TextBox, Slider, ButtonGroup
#//////////////////////////////////////////////////
#Header title
app = App(title="City Gym", height=1200, width=400, layout="auto")
picture = Picture(app, image="citygymlogo.png", grid=[1,0])
text = Text(app, text="City Gym", grid=[1,1])
text = Text(app, text="Membership Form", grid=[1,2])
def open_window():
    window.show()
def close_window():
    window.hide()
def exit_citygym():
    import sys
    sys.exit()
#////////////////////////////////////////////////

#//////////////////////////////////////////////////////
#Customer inputs
text = Text(app, text="", grid=[1,3])
text = Text(app, text="CUSTOMER DETAILS", grid=[1,4])
textbox = TextBox(app, text="First name", grid=[1,5], width=20)
textbox = TextBox(app, text="Last name", grid=[1,6], width=20)
textbox = TextBox(app, text="Address", grid=[1,7], width=20)
textbox =TextBox(app, text="Mobile number", grid=[1,8], width=20)

#///////////////////////////////////////////////////
#Memebership buttons
#text = Text(app, text="Some grid [0,0]", grid=[0,0])
#message = Text(app, text="Enter your name", grid=[0,0])
text = Text(app, text="", grid=[1,9])
text = Text(app, text="MEMBERSHIP DETAILS", grid=[1,10])
text = Text(app, text="Membership Type", grid=[1,11])
but_hex = "#7B61FF"
box = Box(app, layout="grid", grid=[1,12])
button1 = PushButton(box, text="Basic $10pw", grid=[0,1])
button2 = PushButton(box, text="Regular $15pw", grid=[1,1])
button3 = PushButton(box, text="Premium $20pw", grid=[2,1])
button1.bg = but_hex
button2.bg = but_hex
button3.bg = but_hex
#button4 = PushButton(box, text="box 2,1", grid=[1,2])
text = Text(app, text="Membership Duration", grid=[1,13])
box1 = Box(app, layout="grid", grid=[1,14])
button4 = PushButton(box1, text="3 Months", grid=[0,1])
button5 = PushButton(box1, text="12 Months", grid=[1,1])
button6 = PushButton(box1, text="24 Months", grid=[2,1])
button4.bg = but_hex
button5.bg = but_hex
button6.bg = but_hex
#///////////////////////////////////////////////////////////

#Payment options
text = Text(app, text="", grid=[1,15])
text = Text(app, text="PAYMENT OPTIONS", grid=[1,16])
text = Text(app, text="Direct Debt", grid=[1,17])
slider = Slider(app, start=0, end=1, grid=[1,18])
text = Text(app, text="Frequecncy of payments", grid=[1,19])
slider = Slider(app, start=0, end=1, grid=[1,20])
open_button = PushButton(app, text="Open", command=open_window, grid=[1,21])

#New window
window = Window(app, title="Membership form contiuned", height=1200, width=400)

#Extras
text = Text(window, text="", grid=[1,1])
text = Text(window, text="EXTRAS", grid=[1,2])
checkbox = CheckBox(window, text="24/7 Access/$1pw", grid=[1,3])
checkbox = CheckBox(window, text="Personal Trainer/$20pw", grid=[1,4])
checkbox = CheckBox(window, text="Diet Consultation/$20pw", grid=[1,5])
checkbox = CheckBox(window, text="Online Fitness Videos/$2pw", grid=[1,6])
text = Text(window, text="", grid=[1,8])
text = Text(window, text="PAYMENT TOTAL", grid=[1,9])
text = Text(window, text="", grid=[1,10])
listbox = ListBox(window, items=['place holder'], grid=[1,11])
close_button = PushButton(window, text="Close", command=close_window, grid=[1,12])
exit_button = PushButton(window, text="Exit", command=exit_citygym, grid=[1,13])

app.display() 



























import PySimpleGUI as sg
 
col1 = sg.Column([
           [sg.Text('Column 1')],                        
                  ])
 
col2 = sg.Column([
           [sg.Text('Column 2')],
           [sg.Button('Button 1'),sg.Button('Button 2')],          
           [sg.Button('Button 3'),sg.Button('Button4')],                              
                ])
 
layout = [[col1,col2]]
window = sg.Window('Layouts', layout)
 
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
 
window.close()


from tkinter import *
 
root = Tk()     
root.title("Layouts")
 
frame_label1 = Label(root,text = "Column 1")
 
frame_button = LabelFrame(root,text = "Buttons")
frame_label2 = Label(frame_button,text = "Column 2")
button_1 = Button(frame_button,text = "Button 1", width = 15)
button_2 = Button(frame_button,text = "Button 2", width = 15)
button_3 = Button(frame_button,text = "Button 3", width = 15)
button_4 = Button(frame_button,text = "Button 4", width = 15)
 
frame_label1.grid(row=0,column=0)
 
frame_button.grid(row=0,column=1)
frame_label2.grid(row=0,column=0)
 
button_1.grid(row=0,column=1)
button_2.grid(row=0,column=2)
button_3.grid(row=1,column=1)
button_4.grid(row=1,column=2)
 
root.mainloop()