'''014240'''

def code_input():
    global codeInput
    try:
        codeInput =  input("input a letter")
    except ValueError as e:
        print("Please enter a letter")
        code_input()

nameList = ["John","Arana","Suzan","Marsha","Ahmed","Bing"]
firstName = nameList[0]
secondName = nameList[1]
thirdName = nameList[2]
forthName = nameList[3]
fithName = nameList[4]
sixthName = nameList[5]

def upper_case():
    uCode = codeInput.upper
    codeOne = firstName.find(uCode) + 1
    codeTwo = secondName.find(uCode) + 1
    codeThree = thirdName.find(uCode) + 1
    codeFour = forthName.find(uCode) + 1
    codeFive = fithName.find(uCode) + 1
    codeSix = sixthName.find(uCode) + 1
    upperSecertCode = f"{codeOne}{codeTwo}{codeThree}{codeFour}{codeFive}{codeSix}"
    return(upperSecertCode)


def lower_case():
    lCode = codeInput.lower
    codeOne = firstName.find(lCode) + 1
    codeTwo = secondName.find(lCode) + 1
    codeThree = thirdName.find(lCode) + 1
    codeFour = forthName.find(lCode) + 1
    codeFive = fithName.find(lCode) + 1
    codeSix = sixthName.find(lCode) + 1
    lowerSecertCode = f"{codeOne}{codeTwo}{codeThree}{codeFour}{codeFive}{codeSix}"
    return(lowerSecertCode)

code_input()
upper = upper_case()
lower = lower_case()

theSecertCode = upper+lower
print(theSecertCode)