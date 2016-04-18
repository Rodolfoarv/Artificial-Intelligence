from deuces import Card, Evaluator, Deck
import numpy as np
import random

NUMBER_OF_PLAYERS = 6
CROSS_OVER_PROBABILITY = 0.4
MUTATION_PROBABILITY = 0.01

#-------------------------------------------------------------------------------
class Player:
    def __init__(self, hand):
        if (hand == None):
            self.hand = []
        else:
            self.hand = hand

    def __str__ (self):
        return Card.print_pretty_cards(self.hand)

    __repr__ = __str__

#-------------------------------------------------------------------------------

class Population:
    def __init__(self,population,number):
        self.population = population
        self.roulette = []
        self.sum_of_fitness = 0
        self.new_selection = np.array([Player(None) for i in range(NUMBER_OF_PLAYERS)])
        deck = Deck()
        self.new_population = initial_population(NUMBER_OF_PLAYERS,deck)
        self.number = number

    def __str__(self):
        result = "\n\n        ############## Population %d ##############\n" %(self.number)
        bestResult = 0
        evaluator = Evaluator()
        for player_hand in self.population:
            result += str(player_hand) + "\n"
            currentResult = evaluator._five(player_hand.hand)
            if (currentResult > bestResult):
                bestResult = currentResult
        p_class = evaluator.get_rank_class(bestResult)
        result += "\n Best solution:  %s " %(evaluator.class_to_string(p_class))
        return result

    def calculate_roulette(self):
        evaluator = Evaluator()
        for player_hand in self.population:
            fitness = evaluator._five(player_hand.hand)
            self.sum_of_fitness += fitness

        #Calculate roulette values
        for player_hand in self.population:
            fitness = float(evaluator._five(player_hand.hand))
            self.roulette.append(fitness/self.sum_of_fitness*100)

        return self.roulette

    def select_random_chromosomes(self):
        self.calculate_roulette()
        selection = 0
        while selection < NUMBER_OF_PLAYERS:
            for i in range(NUMBER_OF_PLAYERS):
                random_selection = random.randint(0,100)
                if (0 <= random_selection <= self.roulette[i]):
                    self.new_selection[selection] = self.population[i]
                    selection += 1
                    break
        return self.new_selection

    #Cross Over

    #This method determines where will the cross over occur
    def cross_over_position(self):
        position = 0
        crossed = False
        while(not(crossed)):
            if position == NUMBER_OF_PLAYERS:
                position = 0
            random_bit = random.randint(0,100)
            if (0 < random_bit < CROSS_OVER_PROBABILITY*100):
                crossed = True
                return position
            position += 1

    def mutate(self):
        deck = Deck()
        card = deck.draw
        return card

    #Auxiliar method for cross over, this will make the cross over within a chromosome
    #It takes the chromosome1, chromosome2 and the position where the cross over will occur
    #also in this method, the mutation is handled everytime a bit is shifted to the new chromosome
    def cross_over_aux(self,chromosome1,chromosome2,position):
        cross_over = 0
        crossed = False
        deck = Deck()
        hand = deck.draw(5)
        new_chromosome = Player(hand)
        for gene in range(NUMBER_OF_PLAYERS-1):
            if (not(crossed)):
                if (position == cross_over):
                    crossed = True
                #Mutation
                random_mutation = random.randint(0,100)
                if (0 < random_mutation <= MUTATION_PROBABILITY*100):
                    mutated = self.mutate()
                    # new_chromosome.hand[cross_over] = mutated
                    new_chromosome.hand[cross_over] = chromosome1.hand[cross_over]

                else:
                    new_chromosome.hand[cross_over] = chromosome1.hand[cross_over]


            else:
                new_chromosome.hand[cross_over] = chromosome2.hand[cross_over]

            cross_over += 1
        return new_chromosome

    def cross_over(self):
        index = 0
        if (NUMBER_OF_PLAYERS % 2 != 0):
            self.new_population[index] = self.population[index]
            # self.new_population.append(self.population[index])
            index += 1

        while index < NUMBER_OF_PLAYERS:
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

    __repr__ = __str__

class Solution:
    def __init__(self):
        self.populations = []

    def add_population(self, population):
        self.populations.append(population)

    def __str__(self):
        return str(self.populations)

    __repr__ = __str__
#-------------------------------------------------------------------------------


#Method that initializes the first population
def initial_population(no_of_players,deck):
    """Method which is used to initializes the first population, this will be
    the initial setup for the genetic algorithm """

    game_population = np.array([Player(None) for i in range(NUMBER_OF_PLAYERS)])
    for i in range (NUMBER_OF_PLAYERS):
        hand = deck.draw(5)
        player = Player(hand)
        game_population[i] = player
    return game_population

#Generate initial population:

def main():
    deck = Deck()
    board = deck.draw(5)
    solution = Solution()
    currentPopulation = 0
    #Generate initial population
    #Add the new population to the solution
    population = initial_population(NUMBER_OF_PLAYERS,deck)

    init_pop = Population(population, currentPopulation+1)
    solution.add_population(init_pop)

    while (currentPopulation < 10):
        # select chromosomes from the current population to apply cross_over and mutation
        solution.populations[currentPopulation].select_random_chromosomes()
        #Cross over and mutation
        new_population = solution.populations[currentPopulation].cross_over()
        currentPopulation += 1
        pop = Population(new_population, currentPopulation+1)
        solution.add_population(pop)
        print (solution)


if __name__ == "__main__":
    main()
