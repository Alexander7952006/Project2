from API import visualisation as vs
from API import filtration as fl

iterator = iter([((0, 0), (1, 0), (1, 1), (0, 1)), ((1, 1), (1, 2), (2, 2), (2, 1))])
filtered = filter(lambda pol: fl.flt_angle_point(pol, (1, 0)), iterator)
vs.visualise_polygons(filtered)