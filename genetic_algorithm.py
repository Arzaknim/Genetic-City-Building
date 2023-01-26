import math

from city import City
from graphing_service import GraphingService
import random as rnd


class GeneticAlgorithm:

    def __init__(self, algo_params, init_probabilities):
        self.num_cities = algo_params['num_cities']
        self.generations = algo_params['generations']
        self.mutation = algo_params['mutation']
        self.width = algo_params['width']
        self.height = algo_params['height']
        self.population = self.init_population(init_probabilities)

    def run(self):
        for i in range(self.generations):
            self.keep_top_half()
            self.multiply()
            self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
            if (i + 1) % 10 == 0:
                print(f'Best fitness of generation {i+1} out of {self.generations}:')
                print(self.population[0].get_fitness())
                print('--------------')

        best = self.population[0]
        GraphingService().show_graph(best)

    def init_population(self, probabilities):
        result = []
        for i in range(self.num_cities):
            result.append(City(self.height, self.width, probabilities=probabilities))

        return result

    def keep_top_half(self):
        limit = math.floor(self.num_cities/2)
        self.population.sort(key=lambda x: x.get_fitness(), reverse=True)
        self.population = self.population[:limit]

    def single_point_crossover(self, parent1, parent2):
        crossover_point = rnd.randint(1, self.width * self.height)
        part1 = parent1.get_genome()[:crossover_point]
        part2 = parent2.get_genome()[crossover_point:]
        new_genome = part1 + part2
        return City(self.height, self.width, genome=new_genome)

    def mutate(self, individual):
        for i in range(len(individual.get_genome())):
            p = rnd.random()
            if p < self.mutation:
                others = ['1', '2', '3', '4', '5']
                others.remove(individual._genome[i])
                lst = list(individual._genome)
                lst[i] = rnd.choice(others)
                individual._genome = ''.join(lst)

    def multiply(self):
        result = []
        size = self.num_cities - len(self.population)
        while len(result) != size:
            parent_a = rnd.choice(self.population)
            parent_b = rnd.choice(self.population)
            while parent_a is parent_b:
                parent_a = rnd.choice(self.population)
                parent_b = rnd.choice(self.population)

            child = self.single_point_crossover(parent_a, parent_b)
            self.mutate(child)
            result.append(child)

        self.population = self.population + result



