import itertools

def gen_rectangle(coords, space = 0.3):
    """Функция-генератор для генерации бесконечной псследовательности прямоугольников.

    Args:
        coords(tuple): координаты вершин полигона
        space(int or float): рфсстояние между генерируемыми прямоугольниками

    Returns:
        generator object: бесконечный генератор

    Raises:
        ValueError('Полигоны не должны пересекаться!')
        ValueError('В прямоугольнике 4 угла!')
        ValueError('Углы не прямые!')
    """

    if space <= 0:
        raise ValueError('Полигоны не должны пересекаться!')
    if len(coords) != 4:
        raise ValueError('В прямоугольнике 4 угла!')

    sorted_coords = sorted(coords, key = lambda x: (x[0], x[1]))
    if not(abs(sorted_coords[0][0] - sorted_coords[1][0]) ==
           abs(sorted_coords[2][0] - sorted_coords[3][0]) and
           abs(sorted_coords[0][1] - sorted_coords[1][1]) ==
           abs(sorted_coords[2][1] - sorted_coords[3][1])):
        raise ValueError('Длины сторон не соответствуют прямоугольнику!')
    side_a_2 = (abs(sorted_coords[0][0] - sorted_coords[1][0]) ** 2 +
                abs(sorted_coords[0][1] - sorted_coords[1][1]) ** 2)
    side_b_2 = (abs(sorted_coords[0][0] - sorted_coords[2][0]) ** 2 +
                abs(sorted_coords[0][1] - sorted_coords[2][1]) ** 2)
    side_c_2 = (abs(sorted_coords[1][0] - sorted_coords[2][0]) ** 2 +
                abs(sorted_coords[1][1] - sorted_coords[2][1]) ** 2)
    if not side_a_2 + side_b_2 == side_c_2:
        raise ValueError('Углы не прямые!')
    x_side = abs(sorted_coords[0][0] - sorted_coords[3][0])

    positions = itertools.count(start = 0, step=x_side + space)
    for shift in positions:
        yield ((coords[0][0] + shift, coords[0][1]),
            (coords[1][0] + shift, coords[1][1]),
            (coords[2][0] + shift, coords[2][1]),
            (coords[3][0] + shift, coords[3][1])
            )


def gen_triangle(coords, space = 0.3):
    """Функция-генератор для генерации бесконечной псследовательности треугольников.

        Args:
            coords(tuple): координаты вершин полигона
            space(int or float): рфсстояние между генерируемыми треугольниками

        Returns:
            generator object: бесконечный генератор

        Raises:
            ValueError('Полигоны не должны пересекаться!')
            ValueError('В треугольнике 3 угла!')
            ValueError('Не выполнено условие существования треугольника!')
        """

    if space <= 0:
        raise ValueError('Полигоны не должны пересекаться!')
    if len(coords) != 3:
        raise ValueError('В треугольнике 3 угла!')

    srtd = sorted(coords, key = lambda x: (x[0], x[1]))
    side_1 = (abs(srtd[0][0] - srtd[1][0]) ** 2 + abs(srtd[0][1] - srtd[1][1]) ** 2) ** (1 / 2)
    side_2 = (abs(srtd[1][0] - srtd[2][0]) ** 2 + abs(srtd[1][1] - srtd[2][1]) ** 2) ** (1 / 2)
    side_3 = (abs(srtd[0][0] - srtd[2][0]) ** 2 + abs(srtd[0][1] - srtd[2][1]) ** 2) ** (1 / 2)
    sides = sorted([side_1, side_2, side_3])
    if sides[2] >= sides[0] + sides[1]:
        raise ValueError('Не выполнено условие существования треугольника!')
    x_side = abs(srtd[0][0] - srtd[2][0])
    positions = itertools.count(start = 0, step=x_side + space)
    for shift in positions:
        yield ((coords[0][0] + shift, coords[0][1]),
            (coords[1][0] + shift, coords[1][1]),
            (coords[2][0] + shift, coords[2][1]),
            )


def gen_hexagon(coords, space = 0.3):
    """Функция-генератор для генерации бесконечной псследовательности шестиугольников.

        Args:
            coords(tuple): координаты вершин полигона
            space(int or float): рфсстояние между генерируемыми шестиугольников

        Returns:
            generator object: бесконечный генератор

        Raises:
            ValueError('Полигоны не должны пересекаться!')
            ValueError('В шестиугольнике 6 углов!')
            ValueError('Это не правильный шестиугольник!')
        """

    if space <= 0:
        raise ValueError('Полигоны не должны пересекаться!')
    if len(coords) != 6:
        raise ValueError('В шестиугольнике 6 углов!')

    srtd = sorted(coords, key = lambda x: (x[0], x[1]))
    side_set = set()
    side_set.add(round((abs(srtd[0][0] - srtd[1][0]) ** 2 +
                        abs(srtd[0][1] - srtd[1][1]) ** 2) ** (1 / 2), 4))
    side_set.add(round((abs(srtd[0][0] - srtd[2][0]) ** 2 +
                        abs(srtd[0][1] - srtd[2][1]) ** 2) ** (1 / 2), 4))
    side_set.add(round((abs(srtd[1][0] - srtd[3][0]) ** 2 +
                        abs(srtd[1][1] - srtd[3][1]) ** 2) ** (1 / 2), 4))
    side_set.add(round((abs(srtd[2][0] - srtd[4][0]) ** 2 +
                        abs(srtd[2][1] - srtd[4][1]) ** 2) ** (1 / 2), 4))
    side_set.add(round((abs(srtd[5][0] - srtd[4][0]) ** 2 +
                        abs(srtd[5][1] - srtd[4][1]) ** 2) ** (1 / 2), 4))
    side_set.add(round((abs(srtd[5][0] - srtd[3][0]) ** 2 +
                        abs(srtd[5][1] - srtd[3][1]) ** 2) ** (1 / 2), 4))

    if len(side_set) != 1:
        raise ValueError('Это не правильный шестиугольник!')

    x_side = abs(srtd[0][0] - srtd[5][0])
    positions = itertools.count(start = 0, step=x_side + space)
    for shift in positions:
        yield ((coords[0][0] + shift, coords[0][1]),
            (coords[1][0] + shift, coords[1][1]),
            (coords[2][0] + shift, coords[2][1]),
            (coords[3][0] + shift, coords[3][1]),
            (coords[4][0] + shift, coords[4][1]),
            (coords[5][0] + shift, coords[5][1])
            )
