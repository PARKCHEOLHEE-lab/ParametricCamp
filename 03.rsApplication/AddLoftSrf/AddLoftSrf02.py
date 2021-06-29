import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

ref_rec = rg.Rectangle3d(rg.Plane.WorldXY, 50, 50) # Rhino.Geometry.Rectangle3d
rec1 = rs.MoveObject(ref_rec, [-60,-60,0])         # Move -> GUID value retrun -> 2bde2293-5083-4b80-bafd-276cab19ef87 
rec2 = rs.OffsetCurve(rec1, [0,0,0], offset)

dp1 = []
dp2 = []
dpt1 = rs.DivideCurve(rec1, div_no)     # Geometry object
dpt2 = rs.DivideCurve(rec2, div_no)     # Geometry object
for i in range(div_no):
    dp1.append(rs.AddPoint(dpt1[i]))    # GUID list
    dp2.append(rs.AddPoint(dpt2[i]))    # GUID list

lns = []
for i in range(div_no):
    lns.append(rs.AddLine(dpt1[i], dpt2[i]))

dpt3 = []
for i in range(div_no):
    t = rs.CurveDomain(lns[i])[1] / 2
    p = rs.EvaluateCurve(lns[i], t)
    dpt3.append(rs.AddPoint(p))
    rs.MoveObject(dpt3[i], [0,0,z])

crv = [] 
for i in range(div_no):
    crv.append(rs.AddLine(dpt2[i], dpt3[i])) # GUID list

loftsrf = rs.AddLoftSrf(crv, loft_type = l_type, closed=True) # loft_type
rs.CapPlanarHoles(loftsrf)