import math


def tr_translate(polygons, space = None):
    """Параллельный перенос последовательности полигонов

    Args:
        polygons(iter): последовательность полигонов
        space(int or float): расстояние на которое будет сделан перенос

    Returns:
        iter: последовательность перенесенных полигонов
    """

    if space is None:
        list_pol = list(polygons)
        polygons = iter(list_pol)
        side_y = (max([coord[1] for polygon in list_pol for coord in polygon]) -
                  min([coord[1] for polygon in list_pol for coord in polygon])) + 0.3
    else:
        side_y = space
    return (map(lambda polygon: tuple(map(lambda coord:
        (coord[0], coord[1] + side_y), polygon)), polygons))


def tr_symmetry(polygons, space = 0.3):
    """Симметрическое отображение последовательности полигонов

        Args:
            polygons(iter): последовательность полигонов
            space(int or float): Пробел между исходной и симметричной последовательностями

        Returns:
            iter: последовательность симметричных полигонов
        """

    list_pol = list(polygons)
    polygons = iter(list_pol)
    max_y = max([coord[1] for polygon in list_pol for coord in polygon])
    return (map(lambda polygon: tuple(map(lambda coord:
        (coord[0], 2 * max_y - coord[1] + space), polygon)), polygons))


def tr_rotate(polygons, degrees = 45):
    """Ротация последовательности полигонов

        Args:
            polygons(iter): последовательность полигонов
            degrees(int or float): кол-во градусов на которые будет сделан поворот

        Returns:
            iter: последовательность перенесенных полигонов
        """

    angle = math.radians(degrees)
    cos_angle = math.cos(angle)
    sin_angle = math.sin(angle)

    return (map(lambda polygon: tuple(map(lambda coord:
        (coord[0] * cos_angle - coord[1] * sin_angle,
         coord[0] * sin_angle + coord[1] * cos_angle), polygon)), polygons))


def tr_homothety(polygons, k, space=None):
    """Гомотетия последовательности полигонов

        Args:
            polygons(iter): последовательность полигонов
            k(int or float): коефицент подобия
            space(int or float): подобной фигуры относительно исходной

        Returns:
            iter: последовательность перенесенных полигонов
        """

    def center(polygon):
        """Поиск центральной точки полигона

            Args:
                polygon(егзду): полигон

            Returns:
                tuple: центральная точка
            """

        sum_x, sum_y, count = 0, 0, 0
        for point in polygon:
            sum_x += point[0]
            sum_y += point[1]
            count += 1
        return sum_x / count, sum_y / count

    if space is None:
        list_pol = list(polygons)
        polygons = iter(list_pol)
        side_y = (max([coord[1] for polygon in list_pol for coord in polygon]) -
                  min([coord[1] for polygon in list_pol for coord in polygon])) + 0.1
    else:
        side_y = space

    return (map(lambda polygon: tuple(map(lambda point:
        (center(polygon)[0] + k * (point[0] - center(polygon)[0]),
         center(polygon)[1] + k * (point[1] - center(polygon)[1]) + side_y - 1 / 2 * k * side_y),
                                          polygon)), polygons))
