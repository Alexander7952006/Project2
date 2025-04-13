from API import visualisation as vs
from API import geometrical_operations as gp
from API import filtration as fl


polygons = iter([((-4, -8.2), (4, -8.2), (2, -4.2), (-2, -4.2))])
list_first = list(polygons)
list_second = list(gp.tr_homothety(iter(list_first), 1/2))
list_third = list(gp.tr_homothety(iter(list_second), 1/2))
list_forth = list(gp.tr_homothety(iter(list_third), 1/2))
final = iter(list_first + list_second + list_third + list_forth)
list_final = list(final)
symmetry = gp.tr_symmetry(iter(list_final), 1.2)
rotated = gp.tr_rotate(iter(list_final + list(symmetry)), 135)
filtered = filter(lambda pol: fl.flt_short_side(pol, 3.5), rotated)
vs.visualise_polygons(filtered)