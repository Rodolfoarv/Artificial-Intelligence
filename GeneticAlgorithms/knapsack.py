#Rodolfo Andrés Ramírez Valenzuela
#Knapsack Problem
#Genetic Algorithms
# 3/04/16
#Artificial Intelligence

import string
import random
from numpy import ndarray
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
    def __init__(self, capacity, itemsArray):
        self.capacity = capacity
        self.itemsArray = itemsArray
        self.items = [0] * len(itemsArray)

    def add_item(self, item, quantity):
        self.items[item] += quantity


    def fitness(self):
        fitness = 0;
        for i in range(len(self.items)):
            fitness += itemsArray[i].benefit * self.items[i]
        return fitness;

    def __str__(self):
        return str(self.items)


#-------------------------------------------------------------------------------
                                #GENETIC ALGORITHMS

class Population:

    def __init__(self):
        pass

    def fitness():
        pass

    def mutate():
        pass

    def cross_over():
        pass

    def add_chromosome(self, chromosome):
        pass


class Solution:

    def __init__(self):
        self.populations = np.zeros((NUMBER_OF_ITEMS,NUMBER_OF_ITEMS))

    def add_population(self):
        pass

    def statistics(self):
        pass



#-------------------------------------------------------------------------------



def init_population(population):
    #Initialize the first population by randomly generating a population of Size chromosomes
    population[0,0,0] = 1
    population[0,0,1] = 1
    population[0,1,1] = 1

#-------------------------------------------------------------------------------

#populatoin array, tridimensional matrix, denoted by [size][numberOfItems][2]
#Size stands for the number of chromosomes in the population
#numberOfItems stands for the number of items that might be included on the knapsack
#Third dimension is used to form a new generation of chromosomes


#Initialization of the items that will be put into the knapsack
item1 =  Item(1,2)
item2 =  Item(2,4)
item3 =  Item(3,7)
item4 =  Item(7,9)
item5 =  Item(11,13)
item6 =  Item(13,9)
item7 =  Item(17,11)

itemsArray = []
itemsArray.extend([item1, item2, item3, item4, item5, item6, item7])

#Initialization of the knapsack with the default items
knapsack = Knapsack(32, itemsArray)


knapsack.add_item(1,5);

print(knapsack.fitness());

#Initialize the population
# init_population(population)
# print (population)
