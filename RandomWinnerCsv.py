"""++Random Winner.csv++"""
import random as rd
import os
import csv
from random import sample
ori=os.getcwd()

def randomwin():
    """works with .csv file format
       changes dir to file loc, opens file into list
       randomly samples a single name as winner"""
    global winner
    path=f'C:\Python\Inputs'
    file=f'ConTest.csv'
    pydir=path.replace('\\', '/')
    os.chdir(pydir)
    with open(file, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
    winner = rd.sample(data, 1)
    return(winner) 
randomwin()
os.chdir(ori)
print(winner)
