'''014210'''
def secret_code_gen():
    userInput =  input("input a letter").lower()
    nameList = ["John","Arana","Suzan","Marsha","Ahmed","Bing"]
    code = ""
    for name in nameList:
        nameLower = name.lower()
        digit = str(nameLower.find(userInput) + 1)
        code += digit
    return(code)

secret_code = secret_code_gen()
print(secret_code)
