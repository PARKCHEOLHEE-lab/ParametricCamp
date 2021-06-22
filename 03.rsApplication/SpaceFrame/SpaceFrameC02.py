import rhinoscriptsyntax as rs

tls = []
veca = [0,0,0]
vecb = [scale,0,0]

for i in range(1, x-1):
    subvec = rs.VectorSubtract(vecb,veca) * i
    trs = rs.MoveObject(rs.CopyObject(lns1), subvec)
    tls.append(trs)

truss = tls
