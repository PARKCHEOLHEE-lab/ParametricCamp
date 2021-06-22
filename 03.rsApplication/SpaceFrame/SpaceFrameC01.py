import rhinoscriptsyntax as rs

p = rs.AddPoint
pts1 = []
pts2 = []
lns1 = []

for i in range(2):
    for j in range(pNum):
        p1 = p(i * scale, j * scale, z)
        p1 = rs.PointCoordinates(p1)
        pts1.append(p1)

dis = rs.Distance(pts1[0], pts1[1]) / 2

for j in range(2-1):
    for k in range(pNum-1):
        p2 = p(j * scale + dis, k * scale + dis, z/2)
        p2 = rs.PointCoordinates(p2)
        pts2.append(p2)

for i in range(pNum-1):
    ln1 = rs.AddLine(pts1[i],pts2[i])
    ln2 = rs.AddLine(pts1[i+1],pts2[i])
    ln3 = rs.AddLine(pts1[i+pNum],pts2[i])
    ln4 = rs.AddLine(pts1[i+pNum+1],pts2[i])

    lns1.append(ln1)
    lns1.append(ln2)
    lns1.append(ln3)
    lns1.append(ln4)

for i in range(len(pts1)-1):
    if pts1.index(pts1[i]) % pNum == 0:
        ln1 = rs.AddLine(pts1[i], pts1[(i+pNum)-1])
        lns1.append(ln1)

for i in range(int((len(pts1)+1)/2)):
    ln1 = rs.AddLine(pts1[i], pts1[(i+pNum)])
    lns1.append(ln1)
    

scale = scale

pts1
pts2
lns1

