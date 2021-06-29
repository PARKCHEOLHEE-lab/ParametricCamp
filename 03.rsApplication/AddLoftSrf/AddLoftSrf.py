import rhinoscriptsyntax as rs

if rs.IsCurve(crv01):
    crv02 = rs.OffsetCurve(crv01, [0,0,0], -5.0)

div_no = 10

pts01 = []
pts02 = []
pt01 = rs.DivideCurve(crv01, div_no)
pt02 = rs.DivideCurve(crv02, div_no)

for i in range(div_no):
    pts01.append(rs.AddPoint(pt01[i]))
    pts02.append(rs.AddPoint(pt02[i]))

ln = []
for i in range(div_no): ln.append(rs.AddLine(pt01[i],pt02[i]))

pt03 = [] #record of midpts.
for i in range(div_no):
 t = rs.CurveDomain(ln[i])[1] / 2.0
 point = rs.EvaluateCurve(ln[i],t)
 pt03.append(rs.AddPoint(point))
 rs.MoveObject(pt03[i],[0,0,10])
crv = []
for i in range(div_no):
 crv.append(rs.AddArc3Pt(pt01[i],pt02[i],pt03[i]))
b = rs.AddLoftSrf(crv, closed=True)