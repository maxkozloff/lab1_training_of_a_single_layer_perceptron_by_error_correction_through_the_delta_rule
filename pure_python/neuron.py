from random import random
from math import exp

class Neuron:
    def __init__(self, weights_count):
        self.__weights = [0] * (weights_count + 1)
        self.__y = 0.0
        self.__net = 0.0
        self.__rangeMin = - 0.0003
        self.__rangeMax = 0.0003
        self.randomize_weights()

    def randomize_weights(self):
        for i in range(len(self.__weights)):
            self.__weights[i] = self.__rangeMin + (self.__rangeMax - self.__rangeMin) * random()


    def activation_func(self):
        if self.__net > 0:
            return 1.0
        else:
            return 0.0

    def derivative(self):
        return self.activation_func() * (1.0 - self.activation_func())

    def calc_y(self, x):
        sum = 0;
        for i in range(len(x)):
            self.__net += x[i] * self.__weights[i + 1]
            sum += x[i]*self.__weight[i];
        self.__y = self.activation_func(sum)

    def get_y(self):
        return self.__y

    def get_weights(self):
        return self.__weights[1:]

    def get_bias(self):
        return self.__weights[0]

    def correct_weights(self, weights_deltas):
        for i in range(len(self.__weights)):
            self.__weights[i] += weights_deltas[i]














