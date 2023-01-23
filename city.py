from buildings_enum import EntityEnum
from random import choices
import matplotlib.pyplot as plt
import numpy as np


class City:
    RANGE = 5

    def __init__(self, height, width, probabilities):
        self.height = height
        self.width = width
        self.map = self.init_map(probabilities)
        self.fitness = self.calc_fitness()
        self.genome = self.flatten_map()

    def calc_fitness(self):
        fitness = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == EntityEnum.APARTMENTS:
                    has_entertainment = False
                    has_groceries = False
                    has_employment = False

                    for offset in range(1, City.RANGE+1):
                        found = self.local_search(x, y, offset)
                        if found.count(EntityEnum.EMPLOYMENT) > 0 and not has_employment:
                            fitness = fitness + 100/offset
                            has_employment = True
                        if found.count(EntityEnum.ENTERTAINMENT) > 0 and not has_entertainment:
                            fitness = fitness + 50/offset
                            has_entertainment = True
                        if found.count(EntityEnum.GROCERIES) > 0 and not has_groceries:
                            fitness = fitness + 100/offset
                            has_groceries = True

                        if has_employment and has_groceries and has_employment:
                            break

                # TODO road connection of buildings fitness calculation
        return fitness

    def local_search(self, x, y, offset):
        result = []
        top_left_y = y - offset
        top_left_x = x - offset
        for offset_y in range(offset * 2 + 1):
            for offset_x in range(offset * 2 + 1):
                search_x = top_left_x + offset_x
                search_y = top_left_y + offset_y

                if search_y < 0 or search_x > self.width:
                    break
                if (search_x > -1 and search_y > -1) and (search_x < self.width and search_y < self.height) and not (search_x == x and search_y == y):

                    if self.map[search_y][search_x] == EntityEnum.GROCERIES:
                        result.append(EntityEnum.GROCERIES)
                    elif self.map[search_y][search_x] == EntityEnum.EMPLOYMENT:
                        result.append(EntityEnum.EMPLOYMENT)
                    elif self.map[search_y][search_x] == EntityEnum.ENTERTAINMENT:
                        result.append(EntityEnum.ENTERTAINMENT)

        return result

    def flatten_map(self):
        result = ''
        for y in range(self.height):
            for x in range(self.width):
                result = result + str(self.map[y][x].value)

        return result

    def show_graph(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == EntityEnum.EMPTY:
                    pass
                elif self.map[y][x] == EntityEnum.ROAD:
                    plt.plot(np.array([self.height - y]), np.array([self.width - x]), 'o', color='black')
                elif self.map[y][x] == EntityEnum.EMPLOYMENT:
                    plt.plot(np.array([self.height - y]), np.array([self.width - x]), 'o', color='blue')
                elif self.map[y][x] == EntityEnum.ENTERTAINMENT:
                    plt.plot(np.array([self.height - y]), np.array([self.width - x]), 'o', color='red')
                elif self.map[y][x] == EntityEnum.APARTMENTS:
                    plt.plot(np.array([self.height - y]), np.array([self.width - x]), 'o', color='purple')
                elif self.map[y][x] == EntityEnum.GROCERIES:
                    plt.plot(np.array([self.height - y]), np.array([self.width - x]), 'o', color='green')
        plt.show()

    def init_map(self, probabilities):
        result = []
        choices_pop = [
            EntityEnum.GROCERIES, EntityEnum.EMPLOYMENT, EntityEnum.ENTERTAINMENT,
            EntityEnum.APARTMENTS, EntityEnum.ROAD, EntityEnum.EMPTY
        ]

        choices_weights = [
            probabilities[EntityEnum.GROCERIES], probabilities[EntityEnum.EMPLOYMENT],
            probabilities[EntityEnum.ENTERTAINMENT], probabilities[EntityEnum.APARTMENTS],
            probabilities[EntityEnum.ROAD], probabilities[EntityEnum.EMPTY]
        ]

        for y in range(self.height):
            result.append([])
            for x in range(self.width):
                result[y].append(choices(choices_pop, choices_weights)[0])

        return result




