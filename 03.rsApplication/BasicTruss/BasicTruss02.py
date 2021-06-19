import rhinoscriptsyntax as rs

p = rs.AddPoint

pts1 = [rs.PointCoordinates(p(i * scale, 0, z)) for i in range(pNum)]
dis = rs.Distance(pts1[0], pts1[1]) / 2
pts2 = [rs.PointCoordinates(p((i * scale) + dis, 0, z-10)) for i in range(pNum-1)]

lns1 = [rs.AddLine(pts1[p], pts1[p+1]) for p in range(len(pts1)-1)]
lns2 = [rs.AddLine(pts2[p], pts2[p+1]) for p in range(len(pts2)-1)]

lns3 = []
for i in range(len(pts2)):
    lns3.append(rs.AddLine(pts1[i], pts2[i]))
    lns3.append(rs.AddLine(pts1[i+1], pts2[i]))