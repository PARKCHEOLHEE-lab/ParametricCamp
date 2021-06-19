import rhinoscriptsyntax as rs
import random as r
import math

r.seed(0)
pts = []

for i in range(dNum):
    
    epsilon = math.pow(gPow, -math.pow(r.random() * 2, 2) * b)

#    x = (r.random() - 0.5) * int(w) * math.pow(epsilon, pow)
#    y = (r.random() - 0.5) * int(h) * math.pow(epsilon, pow)    
    x = (r.random() - 0.5) * 400 * math.pow(epsilon, pow)
    y = (r.random() - 0.5) * 400 * math.pow(epsilon, pow)
#    z = epsilon * scale
    z = (r.random() - 0.5) * 400 * math.pow(epsilon, pow)
    
    dis = x*x + y*y + z*z
    
    if dis < tDis:      
        p = rs.AddPoint(x,y,z)
        pts.append(p)

a = pts