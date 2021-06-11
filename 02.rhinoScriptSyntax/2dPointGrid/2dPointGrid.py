import rhinoscriptsyntax as rs

# rhino 상에서 z값이 0인 임의의 두 point를 찍고 set하시오

pos0 = rs.PointCoordinates(p0)
pos1 = rs.PointCoordinates(p1)

print(len(pos0))                      # pos0 = [x, y, z]
print(pos0[0], pos0[1], pos0[2])      # x, y, z

print(len(pos1))                      # pos1 = [x, y, z]
print(pos1[0], pos1[1], pos1[2])      # x, y, z

x_interval = (pos1[0] - pos0[0]) / (x_num - 1)
y_interval = (pos1[1] - pos0[1]) / (y_num - 1)
pts = []

for i in range(x_num):
    for j in range(y_num):
        
        x = pos0[0] + x_interval * i 
        y = pos0[1] + y_interval * j
        z = 0
        p = rs.AddPoint(x, y, z)
        
        pts.append(p)
        
a = pts