import random
import Rhino.Geometry as rg
import ghpythonlib.components as gh

O = 1
PLANE = rg.Plane.WorldXY

hexagon_cells, hexagon_points = gh.Hexagonal(plane=PLANE,
                                             size=O,
                                             extent_x=cells,
                                             extent_y=cells-3)

circles = []
vectors = []
for hexagon_point in hexagon_points:
    normal = attractor - hexagon_point
    circle = gh.CircleCNR(center=hexagon_point, normal=normal, radius=O/1.2)
    circle_surface = gh.BoundarySurfaces(edges=circle)
    
    circles.append(circle_surface)
    vectors.append(normal)

