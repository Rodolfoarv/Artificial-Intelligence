#Rodolfo Andrés Ramírez Valenzuela
#Knapsack Problem
#Genetic Algorithms
# 3/04/16
#Artificial Intelligence

import string
import random
import numpy as np

NUMBER_OF_ITEMS = 7
#-------------------------------------------------------------------------------

class Item:
    def __init__(self, volume, benefit):
        self.volume = volume
        self.benefit = benefit

    def __str__(self):
        result = "Volume: %d, Benefit: %d" % (self.volume, self.benefit)
        return result

    __repr__ = __str__


#-------------------------------------------------------------------------------

class Knapsack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.items = [];

    def add_item(self, item):
        self.items.append(item)

    def __str__(self):
        return str(self.items)


#-------------------------------------------------------------------------------


#Genetic Algorithms

def fitness():
    return ""

def mutate():
    return ""





#-------------------------------------------------------------------------------

knapsack = Knapsack(32)

#Initialization of the items that will be put into the knapsack
item1 =  Item(1,2)
item2 =  Item(2,4)
item3 =  Item(3,7)
item4 =  Item(7,9)
item5 =  Item(11,13)
item6 =  Item(13,9)
item7 =  Item(17,11)



print (knapsack)
