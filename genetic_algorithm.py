from city import City


class GeneticAlgorithm:

    def __init__(self, algo_params, init_probabilities):
        self.num_cities = algo_params['algo_params']
        self.generations = algo_params['generations']
        self.mutation = algo_params['mutation']
        self.width = algo_params['width']
        self.height = algo_params['height']
        self.population = self.init_generation(self.height, self.width, init_probabilities)

    def run(self):

        for i in range(self.generations):
            pass

    def init_generation(self, height, width, probabilities):

        result = []
        for i in range(self.num_cities):
            result.append(City(height, width, probabilities))

        return result
