from deuces import Card, Evaluator, Deck
import numpy as np

NUMBER_OF_PLAYERS = 5


#-------------------------------------------------------------------------------
class Player:
    def __init__(self, hand):
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
        self.new_population = np.array([Player(None) for i in range(NUMBER_OF_PLAYERS)])
        self.number = number

    def __str__(self):
        result = "\n\n        ############## Population %d ##############\n" %(self.number)
        for player_hand in self.population:
            result += str(player_hand) + "\n"
        return result

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
    board = deck.draw(1)
    solution = Solution()
    currentPopulation = 0
    #Generate initial population
    #Add the new population to the solution
    population = initial_population(5,deck)
    currentPopulation += 1
    init_pop = Population(population, currentPopulation)
    solution.add_population(init_pop)

    # while (currentPopulation < 50):
        #select chromosomes from the current population to apply cross_over and mutation



    print (solution)






if __name__ == "__main__":
    main()
