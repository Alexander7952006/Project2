from API import visualisation as vs
from API import geometrical_operations as gp
from API import polygon_generator as pg
import itertools


rectangles = itertools.islice(pg.gen_rectangle(((-8, 0), (-8, 1), (-6, 1), (-6, 0)), 0.3), 8)
list_first = list(rectangles)
list_second = list(gp.tr_translate(iter(list_first)))
rotated_first = gp.tr_rotate(iter(list_first), 30)
rotated_second = gp.tr_rotate(iter(list_second), 80)
final = iter(list(rotated_first) + list(rotated_second))
vs.visualise_polygons(final)