from entity_enum import EntityEnum


def local_search_service(city, x, y, offset):
    result = []
    top_left_y = y - offset
    top_left_x = x - offset
    for offset_y in range(offset * 2 + 1):
        for offset_x in range(offset * 2 + 1):
            search_x = top_left_x + offset_x
            search_y = top_left_y + offset_y

            if search_y < 0 or search_x > city.get_width():
                break
            if (search_x > -1 and search_y > -1) and (search_x < city.get_width() and search_y < city.get_height()) and not (search_x == x and search_y == y):

                if city.get_node_at(search_x, search_y) == EntityEnum.GROCERIES:
                    result.append(EntityEnum.GROCERIES)
                elif city.get_node_at(search_x, search_y) == EntityEnum.EMPLOYMENT:
                    result.append(EntityEnum.EMPLOYMENT)
                elif city.get_node_at(search_x, search_y) == EntityEnum.ENTERTAINMENT:
                    result.append(EntityEnum.ENTERTAINMENT)
                elif city.get_node_at(search_x, search_y) == EntityEnum.APARTMENTS:
                    result.append(EntityEnum.APARTMENTS)

    return result
