import rhinoscriptsyntax as rs
import Rhino.Geometry as rg

# -------------------------------------- 01 create rectangle ▼

w = 5 * 4
h = 8 * 4
plane = [-w/2, -h/2, 0]                  # rectangle centroid
angle = 90

rec1 = rs.AddRectangle(plane, w, h)
rec2 = rs.CopyObject(rec1, [0, 0, w*15])
centroid = rs.CurveAreaCentroid(rec1)[1] # return to list
rs.RotateObject(rec1, centroid, angle)

recs = [rec1, rec2]

# -------------------------------------- 02 loft & divide surface ▼

loft = rs.AddLoftSrf(recs)
rs.CapPlanarHoles
u = rs.SurfaceDomain(loft, 0)
v = rs.SurfaceDomain(loft, 1)

pts = []
lns = []
for i in range(w+1):
    for j in range(w+1):
        pt = (i/w, j/w, 0)
        srfP = rs.SurfaceParameter(loft, pt)
        newpt = rs.EvaluateSurface(loft, srfP[0], srfP[1])
        pts.append(rs.AddPoint(newpt))

c = rs.AddCurve(pts[0:w+1], 1)         # base rectangle
h_crvs = []
for i in range(1, w+1):
    h_crv = rs.AddCurve(pts[(w+1)*i:(w+1)*(i+1)], 1)
    h_crvs.append(h_crv)

pcs = []
for i in range(len(pts)-(w+1)):
    pc = rs.PointCoordinates
    pcs.append([pc(pts[i]), pc(pts[i+(w+1)])])

v_crvs = []
for i in range(len(pts)-w-1):
    v_crv = rs.AddCurve(pcs[i], 1)
    v_crvs.append(v_crv)