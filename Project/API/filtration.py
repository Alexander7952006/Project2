def flt_angle_point(polygon, point):
    """Функция для фильтрации полигона по совпадающему с заданным углу

    Args:
        polygon(tuple): полигон
        point(tuple): координаты заданного угла
    """

    if point in polygon:
        return polygon


def flt_short_side(polygon, side):
    """Функция для фильтрации полигона если кратчайшая сторона меньше заданного значения

        Args:
            polygon(tuple): полигон
            side(int or float): заданное значение
        """

    sides = []
    for indx in range(len(polygon)):
        if indx != len(polygon) - 1:
            x_side = abs(polygon[indx][0] - polygon[indx + 1][0])
            y_side = abs(polygon[indx][1] - polygon[indx + 1][1])
            sides.append((x_side ** 2 + y_side ** 2) ** (1 / 2))
    if min(sides) < side:
        return polygon

