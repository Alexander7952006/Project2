from API import visualisation as vs
from API import geometrical_operations as gp
from API import polygon_generator as pg
import itertools


rectangles = itertools.islice(pg.gen_triangle(((-10, 0), (-7, 0), (-8.5, 3)), 0.3), 7)
list_first = list(rectangles)
list_second = list(gp.tr_symmetry(iter(list_first)))
final = iter(list_first + list_second)
vs.visualise_polygons(final)