from genetic_algorithm import GeneticAlgorithm
from entity_enum import EntityEnum


if __name__ == '__main__':

    algo_params = {
        'num_cities': 200,
        'width': 10,
        'height': 10,
        'generations': 200,
        'mutation': 0.01
    }

    init_probabilities = {
        EntityEnum.APARTMENTS: 0.2,
        EntityEnum.EMPLOYMENT: 0.2,
        EntityEnum.ENTERTAINMENT: 0.2,
        EntityEnum.GROCERIES: 0.2,
        EntityEnum.GREENERY: 0.2
    }

    GeneticAlgorithm(algo_params, init_probabilities).run()
