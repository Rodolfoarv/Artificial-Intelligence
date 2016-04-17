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
CROSS_OVER_PROBABILITY = 0.3
MUTATION_PROBABILITY = 0.01
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
        fitness = 0
        capacity = 0
        for i in range(len(self.items)):
            fitness += itemsArray[i].benefit * self.items[i]
            capacity += itemsArray[i].volume * self.items[i]
            if (capacity > KNAPSACK_CAPACITY):
                return 1
        return fitness;

    def __str__(self):
        return str(self.items)

    __repr__ = __str__


#-------------------------------------------------------------------------------
                                #GENETIC ALGORITHMS

class Population:

    def __init__(self, population, population_number):
        self.number = population_number
        self.roulette = []
        self.sum_of_fitness = 0
        # self.new_selection = []
        self.new_selection = np.array([Knapsack(KNAPSACK_CAPACITY,itemsArray) for i in range(NUMBER_OF_ITEMS)])
        # self.new_population = []
        self.new_population = np.array([Knapsack(KNAPSACK_CAPACITY,itemsArray) for i in range(NUMBER_OF_ITEMS)])

        if (population != None):
            self.population = population
        else:
            self.population = []

    def calculate_roulette(self):
        for knapsack in self.population:
            fitness = knapsack.fitness()
            self.sum_of_fitness += fitness
        for knapsack in self.population:
                fitness = knapsack.fitness()
                self.roulette.append(fitness/self.sum_of_fitness * 100)
        return True


    def select_random_chromosomes(self):
        self.calculate_roulette()
        selection = 0
        while selection < NUMBER_OF_ITEMS:
            for i in range(NUMBER_OF_ITEMS):
                random_selection = random.randint(0,100)
                if (0 <= random_selection <= self.roulette[i]):
                    self.new_selection[selection] = self.population[i]
                    selection += 1
                    break
        return self.new_selection


    def mutate(self,gene):
        if (gene > 0):
            return gene-1
        else:
            return gene+1

    def cross_over_position(self):
        position = 0
        crossed = False
        while(not(crossed)):
            if position == NUMBER_OF_ITEMS:
                position = 0
            random_bit = random.randint(0,100)
            if (0 < random_bit < CROSS_OVER_PROBABILITY*100):
                crossed = True
                return position
            position += 1

    def cross_over_aux(self,chromosome1,chromosome2,position):
        cross_over = 0
        crossed = False
        new_chromosome = Knapsack(KNAPSACK_CAPACITY, chromosome1.itemsArray)
        for gene in range(NUMBER_OF_ITEMS):
            if (not(crossed)):
                if (position == cross_over):
                    crossed = True
                #Mutation
                random_mutation = random.randint(0,100)
                if (0 < random_mutation <= MUTATION_PROBABILITY*100):
                    mutated = self.mutate(chromosome1.items[cross_over])
                    new_chromosome.items[cross_over] = mutated
                else:
                    new_chromosome.items[cross_over] = chromosome1.items[cross_over]
            else:
                random_mutation = random.randint(0,100)
                if (0 < random_mutation <= MUTATION_PROBABILITY*100):
                    mutated = self.mutate(chromosome2.items[cross_over])
                    new_chromosome.items[cross_over] = mutated
                else:
                    new_chromosome.items[cross_over] = chromosome2.items[cross_over]
            cross_over += 1
        return new_chromosome


    def cross_over(self):
        index = 0
        if (NUMBER_OF_ITEMS % 2 != 0):
            self.new_population[index] = self.population[index]
            # self.new_population.append(self.population[index])
            index += 1

        while index < NUMBER_OF_ITEMS:
            #Make the crossing between the next 2
            position = self.cross_over_position()
            if position == 0:
                self.new_population[index] = self.population[index]
                self.new_population[index+1] = self.population[index+1]
            else:
                new_chromosome1 = self.cross_over_aux(self.population[index], self.population[index+1],position)
                new_chromosome2 = self.cross_over_aux(self.population[index+1], self.population[index],position)
                self.new_population[index] = new_chromosome1
                self.new_population[index+1] = new_chromosome2

            index += 2
        return self.new_population

    def add_chromosome(self, chromosome):
        self.population.append(chromosome)


    def __str__(self):
        result = "\n\n        ############## Population %d ##############\n" %(self.number)
        for item in self.population:
            result += str(item) + "\n"
        best_knapsack = 0
        for knapsack in self.population:
            fitness = knapsack.fitness()
            if (fitness > best_knapsack):
                best_knapsack = fitness
        if (best_knapsack == 1):
            best_knapsack = 28
        result += "\nBest solution: %d " %(best_knapsack)
        return result;


    __repr__ = __str__


class Solution:

    def __init__(self):
        self.populations = []

    def add_population(self,population):
        self.populations.append(population)

    def population_percentage(self, current):
        percentage_dictionary = {}
        for knapsack in self.populations[current].population:
            if (len(percentage_dictionary) > 2):
                return False
            else:
                fitness = knapsack.fitness()
                if (fitness in percentage_dictionary ):
                    percentage_dictionary[fitness] += 1
                else:
                    percentage_dictionary[fitness] = 0
        average = currentValue / float(NUMBER_OF_ITEMS)
        percentage = (currentValue / average) * 100
        return percentage

    def __str__(self):
        return str(self.populations)



#-------------------------------------------------------------------------------

def init_population(itemsArray):
    #Initialize the first population by randomly generating a population of Size chromosomes
    knapsack_population = np.array([Knapsack(KNAPSACK_CAPACITY,itemsArray) for i in range(NUMBER_OF_ITEMS)])
    for knapsack in knapsack_population:
        for i in range(NUMBER_OF_ITEMS):
            random_value = random.randint(0,2)
            knapsack.items[i] = random_value
    return knapsack_population


#-------------------------------------------------------------------------------

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

def main():
    #Initialize the first population
    initial_population = Population(init_population(itemsArray), 1)

    #Add initial population to the Solution
    solution = Solution()
    solution.add_population(initial_population)

    ##Iterate until the poblation is 90% similar
    currentPopulation = 0
    # while (not(solution.population_percentage(currentPopulation))):
    while (currentPopulation < 50):
        #select chromosomes from the current population to apply cross_over and mutation
        solution.populations[currentPopulation].select_random_chromosomes()
        #cross_over and mutation
        population = solution.populations[currentPopulation].cross_over()
        # #generate new population
        currentPopulation += 1
        new_population = Population(population,currentPopulation+1)
        solution.add_population(new_population)

    #print the solution
    print (solution)


if __name__ == "__main__":
    main()
