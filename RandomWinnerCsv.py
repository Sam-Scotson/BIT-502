import random as rd
import os
import csv

ori = os.getcwd()

def randomwin():
    """Works with .csv file format.
    Changes dir to file location, opens file into list, 
    and randomly samples a single name as the winner."""
    path = 'C:/example'  # Replace with your file path
    file = 'WinList.csv'
    pydir = path.replace('\\', '/')
    os.chdir(pydir)
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    winner = rd.sample(data, 1)
    return winner[0]

randomwin()
os.chdir(ori)
print("Random Winner:", winner)
