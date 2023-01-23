from genetic_algorithm import GeneticAlgorithm
from buildings_enum import EntityEnum


if __name__ == '__main__':

    algo_params = {
        'num_cities': 100,
        'width': 10,
        'height': 10,
        'generations': 250,
        'mutation': 0.005
    }

    init_probabilities = {
        EntityEnum.APARTMENTS: 0.08,
        EntityEnum.EMPLOYMENT: 0.06,
        EntityEnum.ENTERTAINMENT: 0.08,
        EntityEnum.GROCERIES: 0.06,
        EntityEnum.ROAD: 0.2,
        EntityEnum.EMPTY: 0.5
    }

    GeneticAlgorithm(algo_params, init_probabilities).run()
