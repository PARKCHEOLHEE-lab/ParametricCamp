import Rhino.Geometry as rg

VEC_SCALE = 5
U_DIVIDER = 1 / u_num
V_DIVIDER = 1 / v_num

evaluate_srf_points = []
normal_srf_points = []
normal_srf_lines = []
normal_srf_pipes = []

for u in range(u_num-1):
    u = (u / u_num) + U_DIVIDER
    
    for v in range(v_num-1):
        v = (v / v_num) + V_DIVIDER
    
        evaluate_point = srf.PointAt(u, v)
        evaluate_srf_points.append(evaluate_point)
        
        normal_srf_vector = srf.NormalAt(u, v) * VEC_SCALE
        normal_srf_point = (evaluate_point + normal_srf_vector)
        normal_srf_points.append(normal_srf_point)
        
        normal_srf_line = rg.Line(evaluate_point, normal_srf_point)
        normal_srf_lines.append(normal_srf_line)
