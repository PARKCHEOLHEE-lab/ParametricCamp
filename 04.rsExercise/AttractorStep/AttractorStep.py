import Rhino.Geometry as rg
import ghpythonlib.components as gh

interval = rg.Interval(-0.5, 0.5)

grid_step = []
for x in range(x_count):
    for y in range(y_count):
        origin = rg.Point3d(x, y, 0)
        cell_crv = gh.Rectangle(origin, interval, interval, 0).rectangle
        cell_centroid = cell_crv.Center
        
        distance_to_attractor = cell_centroid.DistanceTo(attractor)
        step = gh.Extrude(cell_crv, rg.Point3d(0, 0, distance_to_attractor))
        capped_step = gh.CapHoles(step)
        
        grid_step.append(capped_step)