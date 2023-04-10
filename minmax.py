'''min/max'''

digits = [3,6,2,7,8,1]        

def min_max():
    global maxValue, minValue
    maxValue = digits[0]   
    minValue = digits[0]          

    for n in digits:
        if(n > maxValue):         
            maxValue = n    
        elif(n < minValue):
            minValue = n  
    return(maxValue, minValue)

min_max()

print("Max Value = " + str(maxValue))
print("Min Value = " + str(minValue))