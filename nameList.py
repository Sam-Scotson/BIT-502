'''List Append'''

names = []

def name_input():
    global nameInput
    nameInput = input("enter name")

def name_list():   
    name_input()
    if nameInput == '*':
        import sys
        sys.exit()
    else:
        names.append(nameInput)
        name_list()

name_list()

'''count while'''

def hello_display():
    print("How are you?")

#Your initial code
c = 0
name = input("Enter your name: ")
print("Hi " + name)
while c <3:
    hello_display()
    c = c + 1
print("Bye for now!")
