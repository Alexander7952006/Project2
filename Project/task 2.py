import itertools
from API import polygon_generator as polgen
from API import visualisation as vs

hexagons = itertools.islice(polgen.gen_hexagon(((1, 1), (2, 2), (2 + 2 ** (1 / 2), 2), (3 + 2 ** (1 / 2), 1), (2 + 2 ** (1 / 2), 0), (2, 0)), 0.3), 2)
triangles = itertools.islice(polgen.gen_triangle(((9, 0), (10, 0), (9, 1)), 0.3), 3)
rectangles = itertools.islice(polgen.gen_rectangle(((13, 1), (14, 1), (14, 0), (13, 0)), 0.3), 3)
vs.visualise_polygons(iter(list(hexagons) + list(triangles) + list(rectangles)))