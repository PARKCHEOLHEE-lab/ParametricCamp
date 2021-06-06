import rhinoscriptsyntax as rs

pts = []                              # AddPoint를 담을 empty point list
refp = rs.PointCoordinates(p)         # reference point의 좌표값 검색
print(refp[0])                        # x-coordinate
print(refp[1])                        # y-coordinate

for i in range(x+1):
    for j in range(x+1):
        p = rs.AddPoint(i,j,0)
        pts.append(p)
        
        dis = rs.Distance(refp, p)    # point1과 point2간의 distance value return
        rs.MoveObject(p, (0,0,dis))   # rs.Distance()를 통해 얻어낸 값을 통해
                                      # refp와 멀리 있을 수록 z값을 move