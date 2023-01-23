from city import City
from buildings_enum import EntityEnum


class GeneticAlgorithm:

    def __init__(self, algo_params, init_probabilities):
        self.num_cities = algo_params['num_cities']
        self.generations = algo_params['generations']
        self.mutation = algo_params['mutation']
        self.width = algo_params['width']
        self.height = algo_params['height']
        self.population = self.init_generation(self.height, self.width, init_probabilities)

    def run(self):
        self.population[0].show_graph()
        # for i in range(self.generations):
        #     pass

    def init_generation(self, height, width, probabilities):

        result = []
        for i in range(self.num_cities):
            result.append(City(height, width, probabilities))

        return result
