from API import visualisation as vs
from API import filtration as fl

iterator = iter([((0, 0), (1, 2), (3, 2), (4, 0)), ((0, 0), (0, 10), (10, 10), (10, 0))])
filtered = filter(lambda pol: fl.flt_short_side(pol, 3), iterator)
vs.visualise_polygons(filtered)