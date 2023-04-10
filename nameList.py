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


