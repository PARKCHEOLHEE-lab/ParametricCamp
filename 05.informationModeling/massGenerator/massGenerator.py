import Rhino.Geometry as rg
import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
import random as r

file = open(teheran, "r")
columns = file.readline().split(",")
columns = columns[1:]
data = file.readlines()
file.close()

massInfo = []
for i in range(len(data)):
    height = data[i].replace("\n", "").split("POLYGON")[0]
    height = float(height.split(",")[10])
    if height >= 1000:
        height = 0
    elif height == 0:
        height = r.uniform(1.8, 5.3)
        
    polygon = data[i].replace("\n", "").split("POLYGON")[1]
    polygon = polygon.replace("(", "").replace(")", "").replace('"', "").replace(",", "").strip()
    polygon = map(float, polygon.split(" "))
    
    massInfo.extend([[polygon, height]])

pts = []
for i in range(len(massInfo)):
    for j in range(0, len(massInfo[i][0])-1, 2):
        pts.append(rs.AddPoint(massInfo[i][0][j], massInfo[i][0][j+1], 0))

CRV = []
s = 0
for i in range(len(massInfo)):
    pCount = int(len(massInfo[i][0])/2)
    if i == 0:
        s += pCount
        Pts = pts[:pCount]
        CRV.append(rs.AddCurve(Pts, 1))
    else:
        s += pCount
        Pts = pts[s-pCount:s]
        CRV.append(rs.AddCurve(Pts, 1))

bdgs = []
H = []
for i in range(len(massInfo)):
    h = massInfo[i][1]
    if h >= 400:
        h = r.uniform(1.8, 5.3)
        
    base = CRV[i]
    path = rs.AddLine(rs.AddPoint(0,0,0), rs.AddPoint(0,0,h))
    
    building = rs.ExtrudeCurve(base, path)
    rs.CapPlanarHoles(building)
    bdgs.append(building)
    H.append(h)

#H.sort(reverse=True)
#print(H[:3])