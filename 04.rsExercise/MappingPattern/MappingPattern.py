import math
import random
import Rhino.Geometry as rg
import Rhino.RhinoDoc as rc
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh


class Pattern:
    def __init__(self, rectangle, action):
        self._rectangle = rectangle
        self._action = action
        
        self.pattern = None
        self.centroid = None
        self.wall = None
        
    @property
    def rectangle(self):
        return self._rectangle
        
    @property
    def action(self):
        return self._action
        
    def get_rectangle_vertices(self):
        rectangle = self.rectangle
        _, _, rectangle_vertices = gh.DeconstructBrep(rectangle)
        
        return rectangle_vertices
        
    def gen_pattern(self):
        rectangle_vertices = self.get_rectangle_vertices()
        
        v1, v2 = rectangle_vertices[0], rectangle_vertices[2]
        if self.action:
            v1, v2 = rectangle_vertices[1], rectangle_vertices[3]
            
        pattern = rg.Line(v1, v2)
        self.pattern = pattern
        
    def gen_centroid(self):
        rectangle_vertices = self.get_rectangle_vertices()
        self.centroid = rectangle_vertices[0]*0.5 + rectangle_vertices[2]*0.5
        
    def gen_wall(self):
        self.wall = gh.Extrude(base=self.pattern, direction=rg.Point3d(0,0,10))


if __name__ == "__main__":
    
    random.seed(0)
    if reset:
        random.seed(random.randint(1, 500))
    
    SIZE = 15
    CELL = 20
    
    rectangles = []
    patterns = []
    centroids = []
    actions = []
    walls = []
    for x in range(CELL):
        for y in range(CELL):
            
            action = random.randint(0, 1)
            
            origin = rg.Point3d(x*SIZE, y*SIZE, 0)
            rectangle, _ = gh.Rectangle(plane=origin,
                                        x_size=SIZE,
                                        y_size=SIZE,
                                        radius=0)
                                        
            pattern = Pattern(rectangle, action)
            pattern.gen_pattern()
            pattern.gen_centroid()
            pattern.gen_wall()
            
            rectangles.append(rectangle)
            patterns.append(pattern.pattern)
            centroids.append(pattern.centroid)
            actions.append(pattern.action)
            walls.append(pattern.wall)
