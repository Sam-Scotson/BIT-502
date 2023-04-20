'''
Pizza App Ex BIT502
'''
global pizza_id
pizza_id = 23456
import os
import time as t
clear = lambda: os.system('cls')

class Pizza:

    def __init__(self,id_number,pizza_name,pizza_type,pizza_size):
        self.id = id_number
        self.name = pizza_name
        self.type = pizza_type
        self.size = pizza_size

    def eat_pizza(self):
        pizzaSlicesLeft = 8
        while pizzaSlicesLeft > 0:
            print("Yummy!!!!")
            t.sleep(2)
            pizzaSlicesLeft -= 1
            if pizzaSlicesLeft == 0:
                print("No more pizza =(")

def order_input(pizzaFlavs, pizzaType, pizzaSize):
    global pizza_name, pizza_type, pizza_size
    t.sleep(2)
    clear()
    print('please select pizza flavour from the following')
    for flavs in pizzaFlavs:
        print(flavs)
    pizza_pick = int(input('select a number from the above i.e 1 or 2'))
    pizza_name = pizzaFlavs[pizza_pick-1]
    print('Great choice!')
    t.sleep(2)
    clear()
    print('Select a type of pizza from the following')
    for types in pizzaType:
        print(types)
    type_pick = int(input('select a number from the above i.e 1 or 2'))
    pizza_type = pizzaType[type_pick-1]
    print('Gothcha!')
    t.sleep(2)
    clear()
    print('Select a pizza size from the following')
    for sizes in pizzaSize:
        print(sizes)
    size_pick = int(input('select a number from the above i.e 1 or 2'))
    pizza_size = pizzaSize[size_pick-1]

def make_pizza(pizza_name, pizza_type, pizza_size):
    global pizzaSlicesLeft, pizzaPie, id_number
    id_number = str(pizza_id + 1)
    pizzaPie = Pizza(id_number,pizza_name,pizza_type,pizza_size)
    pizzaSlicesLeft = 8
    return(pizzaPie)

def main():

    pizzaFlavs = ['1)-Meat_lovers $30', '2)-Margherita $25', '3)-Italian $20', '4)-Veggie lovers $30', '5)-Classic veggie $25']
    pizzaType = ['1)-Standard', '2)-Vegetarian $2', '3)-Gluten-free $5']
    pizzaSize = ['1)-Small', '2)-Medium $5', '3)-Large $10']
    print('Welcome to the pizza_lab (>)')
    cust_name = input('Please enter your name for order')
    order_input(pizzaFlavs, pizzaType, pizzaSize)
    print('Thanks for that '+cust_name+'!')
    clear()
    print('Making your pizza now! =)')
    make_pizza(pizza_name, pizza_type, pizza_size)
    print('all done!')
    print('Pizza ID Number='+id_number+' - Your pizza order is 1/Flavour='+pizza_name+' 2/Type='+pizza_type+' 3//Size='+pizza_size)
    pizza_cost = 0
    if '3)-Large $10' in pizza_size:
        pizza_cost += 10
    elif '2)-Medium $5' in pizza_size:
        pizza_cost += 5
    elif '1)-Small' in pizza_size:
        pizza_cost += 0

    if '1)-Meat_lovers $30' in pizza_name:
        pizza_cost += 30
    elif '2)-Margherita $25' in pizza_name:
        pizza_cost += 25
    elif '3)-Italian $20' in pizza_name:
        pizza_cost +=20
    elif '4)-Veggie lovers $30' in pizza_name:
        pizza_cost += 30
    elif '5)-Classic veggie $25' in pizza_name:
        pizza_cost += 25

    if '1)-Standard' in pizza_type:
        pizza_cost += 0
    elif '2)-Vegetarian $2' in pizza_type:
        pizza_cost += 2
    elif '3)-Gluten-free $5' in pizza_type:
        pizza_cost += 5

    totalPizzaCost = str(pizza_cost)
    print('total cost is...')
    print(pizza_name)
    print(pizza_size)
    print(pizza_type)
    print('Total=$'+totalPizzaCost)
    print('Opening payments now')

main()
pizzaPie.eat_pizza()
