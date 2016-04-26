import numpy as np
import numpy.random as npr
import sys

import flappy as game

class QLearning:

    def __init__(self, actions, epsilon=0.1, alpha=0.2, gamma=0.9):
        self.q = {}

        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.actions = actions

    def getQ(self, state, action):
        pass

    def learn_q(self, state, action, reward, value):
        pass

    def choose_action(self, state):
        pass

    def learn(self, state1, action, reward, state2):
        pass
