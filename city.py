from entity_enum import EntityEnum
from random import choices
from local_search_service import local_search_service


class City:
    RANGE = 2
    GREENERY_VALUE = 50

    def __init__(self, height, width, probabilities=None, genome=None):
        self._height = height
        self._width = width

        if genome is None:
            self._genome = self._init_genome(probabilities)
        elif probabilities is None:
            self._genome = genome

        self._map = self._create_map_from_genome()
        self._fitness = self._calc_fitness()

    def _calc_fitness(self):
        fitness = 0
        greenery = 0
        apts = 0
        for y in range(self._height):
            for x in range(self._width):
                if self._map[y][x] == EntityEnum.GREENERY:
                    greenery = greenery + 1
                    for offset in range(1, City.RANGE+1):
                        found = local_search_service(self, x, y, offset=1)
                        if found.count(EntityEnum.GREENERY) > 1:
                            fitness = fitness + 20
                elif self._map[y][x] == EntityEnum.APARTMENTS:
                    apts = apts + 1
                    has_entertainment = False
                    has_groceries = False
                    has_employment = False

                    for offset in range(1, City.RANGE+1):
                        found = local_search_service(self, x, y, offset)
                        if found.count(EntityEnum.EMPLOYMENT) > 0 and not has_employment:
                            fitness = fitness + 20
                            has_employment = True
                        if found.count(EntityEnum.ENTERTAINMENT) > 0 and not has_entertainment:
                            fitness = fitness + 20
                            has_entertainment = True
                        if found.count(EntityEnum.GROCERIES) > 0 and not has_groceries:
                            fitness = fitness + 20
                            has_groceries = True
                        if found.count(EntityEnum.APARTMENTS) > 1:
                            fitness = fitness - 100 * (found.count(EntityEnum.APARTMENTS) - 1)

                        if has_employment and has_groceries and has_employment and found.count(EntityEnum.APARTMENTS) == 1:
                            fitness = fitness + 500
                            break
        apts_bonus = 0
        if apts > 10:
            apts_bonus = 2000
        greenery_bonus = greenery * City.GREENERY_VALUE
        fitness = fitness + greenery_bonus + apts_bonus
        return fitness

    def _init_genome(self, probabilities):
        choices_pop = [
            EntityEnum.GROCERIES, EntityEnum.EMPLOYMENT, EntityEnum.ENTERTAINMENT,
            EntityEnum.APARTMENTS, EntityEnum.GREENERY
        ]

        choices_weights = [
            probabilities[EntityEnum.GROCERIES], probabilities[EntityEnum.EMPLOYMENT],
            probabilities[EntityEnum.ENTERTAINMENT], probabilities[EntityEnum.APARTMENTS],
            probabilities[EntityEnum.GREENERY]
        ]

        result = ''
        for idx in range(self._height * self._width):
            choice = str(choices(choices_pop, choices_weights)[0].value)
            result = result + choice

        return result

    def _create_map_from_genome(self):
        result = []

        for y in range(self._height):
            result.append([])
            for x in range(self._width):
                idx = y * self._width + x
                entity = None
                if self._genome[idx] == '1':
                    entity = EntityEnum.GREENERY
                elif self._genome[idx] == '2':
                    entity = EntityEnum.GROCERIES
                elif self._genome[idx] == '3':
                    entity = EntityEnum.APARTMENTS
                elif self._genome[idx] == '4':
                    entity = EntityEnum.ENTERTAINMENT
                if self._genome[idx] == '5':
                    entity = EntityEnum.EMPLOYMENT
                result[y].append(entity)

        return result

    def get_genome(self):
        return self._genome

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_fitness(self):
        return self._fitness

    def get_node_at(self, x, y):
        return self._map[y][x]

