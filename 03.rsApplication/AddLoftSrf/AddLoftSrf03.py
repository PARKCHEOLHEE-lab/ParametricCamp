import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

cir = rs.AddCircle([0,0,100], rad)
rec = rs.MoveObject(rg.Rectangle3d(rg.Plane.WorldXY, 50, 50), [-25,-25,0])

cpt = []
rpt = []
cp = rs.DivideCurve(cir, div_no)
rp = rs.DivideCurve(rec, div_no)

for i in range(div_no):
    cpt.append(rs.AddPoint(cp[i]))
    rpt.append(rs.AddPoint(rp[i]))

lns = []
for i in range(div_no):
    lns.append(rs.AddLine(cpt[i], rpt[i]))

loft = rs.AddLoftSrf(lns, loft_type = l_type, closed=True)

a = cir
b = rec
c = cp
d = rp
e = lns
f = loft