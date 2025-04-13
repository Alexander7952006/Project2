from API import wrappers as wp
import matplotlib.pyplot as plt


polygons = iter([((-4, -8.2), (4, -8.2), (2, -4.2), (-2, -4.2))])

@wp.dec_tr_translate(10)
def visualise_polygons(iterable_polygons):
    """Функция для визуализации последовательности полигонов.

        Args:
             iterable_polygons(iter): итерируемый объект хранящий полигоны вида ((x1, y1)...)
        """

    polygons = list(iterable_polygons)

    if len(polygons) == 0:
        raise ValueError('Вы не дали данные на вход')

    for polygon in polygons:
        if len(polygon) < 3:
            raise ValueError('Это не полигон')

    fig, ax = plt.subplots(figsize=(8, 8))

    ax.spines['left'].set_position('center')
    ax.spines['bottom'].set_position('center')
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.plot(1, 0, 'k>', transform=ax.get_yaxis_transform(), clip_on=False)
    ax.plot(0, 1, 'k^', transform=ax.get_xaxis_transform(), clip_on=False)
    ax.set_xticks([])
    ax.set_yticks([])

    border = []
    for polygon in polygons:
        sorted_by_x = sorted(polygon, key = lambda x: x[0])
        sorted_by_y = sorted(polygon, key = lambda x: x[1])
        border.append(abs(sorted_by_x[0][0]))
        border.append(abs(sorted_by_x[len(polygon) - 1][0]))
        border.append(abs(sorted_by_y[0][1]))
        border.append(abs(sorted_by_y[len(polygon) - 1][1]))
    ax.set_xlim(-1 - max(border), 1 + max(border))
    ax.set_ylim(-1 - max(border), 1 + max(border))

    for polygon in polygons:
        x = [coord[0] for coord in polygon]
        y = [coord[1] for coord in polygon]
        x_closed = x + [x[0]]
        y_closed = y + [y[0]]
        ax.plot(x_closed, y_closed, linewidth=1, color = 'blue')
    plt.show()

visualise_polygons(polygons)