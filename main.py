from genetic_algorithm import GeneticAlgorithm
from buildings_enum import BuildingEnum


if __name__ == '__main__':

    algo_params = {
        'num_cities': 100,
        'width': 10,
        'height': 10,
        'generations': 250,
        'mutation': 0.005
    }

    init_probabilities = {
        BuildingEnum.APARTMENTS: 0.001,
        BuildingEnum.EMPLOYMENT: 0.005,
        BuildingEnum.ENTERTAINMENT: 0.02,
        BuildingEnum.GROCERIES: 0.01,
        BuildingEnum.ROAD: 0.05,
    }

    GeneticAlgorithm(algo_params, init_probabilities).run()
