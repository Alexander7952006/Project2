from API import visualisation as vs
from API import geometrical_operations as gp
from API import polygon_generator as pg
import itertools


rectangles = itertools.islice(pg.gen_rectangle(((-8, 0), (-8, 1), (-6, 1), (-6, 0)), 0.3), 8)
list_first = list(rectangles)
list_second = list(gp.tr_translate(iter(list_first)))
list_third = list(gp.tr_translate(iter(list_second)))
parallel = iter(list_first + list_second + list_third)
rotated = gp.tr_rotate(parallel, 30)
vs.visualise_polygons(rotated)



