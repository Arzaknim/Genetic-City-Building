from entity_enum import EntityEnum
from city import City
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np


class GraphingService:

    def show_graph(self, city: City):
        for y in range(city.get_height()):
            for x in range(city.get_width()):
                self._write_node(city, x, y)

        self._create_legend_for_graph()
        plt.show()

    def _create_legend_for_graph(self):
        legend_elements = [Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=10),
                           Line2D([0], [0], marker='o', color='w', markerfacecolor='yellow', markersize=10),
                           Line2D([0], [0], marker='o', color='w', markerfacecolor='purple', markersize=10),
                           Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10),
                           Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10)]
        plt.legend(legend_elements, ['Grass', 'Food', 'Apts', 'Fun', 'Job'],
                   loc='upper center', bbox_to_anchor=(0.5, -0.05),
                   fancybox=True, shadow=True, ncol=6
                   )

    def _write_node(self, city, x, y):
        if city.get_node_at(x, y) == EntityEnum.GREENERY:
            plt.plot(np.array([city.get_height() - y]), np.array([city.get_width() - x]), 'o', color='green')
        elif city.get_node_at(x, y) == EntityEnum.EMPLOYMENT:
            plt.plot(np.array([city.get_height() - y]), np.array([city.get_width() - x]), 'o', color='blue')
        elif city.get_node_at(x, y) == EntityEnum.ENTERTAINMENT:
            plt.plot(np.array([city.get_height() - y]), np.array([city.get_width() - x]), 'o', color='red')
        elif city.get_node_at(x, y) == EntityEnum.APARTMENTS:
            plt.plot(np.array([city.get_height() - y]), np.array([city.get_width() - x]), 'o', color='purple')
        elif city.get_node_at(x, y) == EntityEnum.GROCERIES:
            plt.plot(np.array([city.get_height() - y]), np.array([city.get_width() - x]), 'o', color='yellow')