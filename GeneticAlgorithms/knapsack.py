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
KNAPSACK_CAPACITY = 32
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

    __repr__ = __str__


#-------------------------------------------------------------------------------
                                #GENETIC ALGORITHMS

class Population:

    def __init__(self, population, population_number):
        self.population = population
        self.number = population_number

    def fitness():
        pass

    def mutate():
        pass

    def cross_over():
        pass

    def add_chromosome(self, chromosome):
        pass

    def __str__(self):
        result = "\n\n        ############## Population %d ##############\n" %(self.number)
        for item in self.population:
            result += str(item) + "\n"
        return result;


    __repr__ = __str__


class Solution:

    def __init__(self):
        self.populations = []

    def add_population(self,population):
        self.populations.append(population)

    def statistics(self):
        pass

    def __str__(self):
        return str(self.populations)



#-------------------------------------------------------------------------------

def init_population(itemsArray):
    #Initialize the first population by randomly generating a population of Size chromosomes

    #Initialization of the knapsack with the default items
    knapsack = Knapsack(KNAPSACK_CAPACITY, itemsArray)
    knapsack_population = np.array([Knapsack(KNAPSACK_CAPACITY,itemsArray) for i in range(NUMBER_OF_ITEMS)])
    for knapsack in knapsack_population:
        for i in range(NUMBER_OF_ITEMS):
            random_value = random.randint(1,5)
            knapsack.items[i] = random_value

    return knapsack_population


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

#Initialize the first population
initial_population = Population(init_population(itemsArray), 1)

#Add initial population to the Solution
solution = Solution()
solution.add_population(initial_population)
print (solution)
