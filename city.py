from buildings_enum import BuildingEnum
from random import choices


class City:
    RANGE = 5

    def __init__(self, height, width, probabilities):
        self.height = height
        self.width = width
        self.world = []
        choices_pop = [
            BuildingEnum.GROCERIES, BuildingEnum.EMPLOYMENT, BuildingEnum.ENTERTAINMENT,
            BuildingEnum.APARTMENTS, BuildingEnum.ROAD
        ]

        choices_weights = [
            probabilities[BuildingEnum.GROCERIES], probabilities[BuildingEnum.EMPLOYMENT],
            probabilities[BuildingEnum.ENTERTAINMENT], probabilities[BuildingEnum.APARTMENTS],
            probabilities[BuildingEnum.ROAD]
        ]

        for y in range(height):
            self.world[y] = []
            for x in range(width):
                self.world[y][x] = choices(choices_pop, choices_weights)
        self.genome = ''

    def calc_fitness(self):
        fitness = 0
        for y in range(self.height):
            for x in range(self.width):
                if self.world[y][x] == BuildingEnum.APARTMENTS:
                    has_entertainment = False
                    has_groceries = False
                    has_employment = False

                    for offset in range(City.RANGE):
                        found = self.local_search(x, y, offset)
                        if found.count(BuildingEnum.EMPLOYMENT) > 0 and not has_employment:
                            fitness = fitness + 100/offset
                            has_employment = True
                        if found.count(BuildingEnum.ENTERTAINMENT) > 0 and not has_entertainment:
                            fitness = fitness + 50/offset
                            has_entertainment = True
                        if found.count(BuildingEnum.GROCERIES) > 0 and not has_groceries:
                            fitness = fitness + 100/offset
                            has_groceries = True

                        if has_employment and has_groceries and has_employment:
                            break

                # TODO road connection of buildings fitness calculation

    def local_search(self, x, y, offset):
        result = []
        top_left_y = y - offset
        top_left_x = x = offset
        for offset_y in range(offset * 2 + 1):
            for offset_x in range(offset * 2 + 1):
                search_x = top_left_x + offset_x
                search_y = top_left_y + offset_y
                if (search_x > -1 and search_y > -1) and (search_x != x and search_y != y):
                    if self.world[search_y][search_x] == BuildingEnum.GROCERIES:
                        result.append(BuildingEnum.GROCERIES)
                    elif self.world[search_y][search_x] == BuildingEnum.EMPLOYMENT:
                        result.append(BuildingEnum.EMPLOYMENT)
                    elif self.world[search_y][search_x] == BuildingEnum.ENTERTAINMENT:
                        result.append(BuildingEnum.ENTERTAINMENT)

        return result



