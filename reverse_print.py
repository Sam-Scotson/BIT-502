import os
import math
loc = 'C:/Users/Sam/Documents/OpenPoly/BIT502Ass2/'
def reverse_print(loc):
    
    os.chdir(loc)

    with open(loc+'education_journey.txt', 'r', encoding="utf8") as f:
        lines = list(f.readlines())
        cursor = 1
        for line in lines:
            print(lines[-+cursor])
            cursor += 1

reverse_print(loc)



