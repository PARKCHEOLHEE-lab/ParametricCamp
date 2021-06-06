import rhinoscriptsyntax as rs

pts = []                              # AddPoint를 담을 empty point list

for i in range(x+1):
    for j in range(x+1):
        p = rs.AddPoint(i,j,0)
        pts.append(p)