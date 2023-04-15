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

#
def people_input():
    global name,age,vaccine
    name = input('enter name')
    age = int(input('enter age'))
    vaccine = input('do you have a vaccine pass (y/n').lower


def people_sort(name, age, vaccine):
    if age < 18:
        print(name+', you are not eligible to attend.')
        import sys
        sys.exit()
    elif age >= 50 and vaccine == 'y':
        print(name+', go to hall A / Category 1')
    elif age >= 50 and vaccine == 'n':
        print(name+', go to hall B / Category 2')
    else:
        print(name+', go to hall C / Category 3')

people_input()
people_sort(name, age, vaccine)
