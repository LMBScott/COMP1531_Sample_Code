class Line_Segment():
    def __init__(self, point_a, point_b):
        self.ends = (point_a, point_b)

        a_x, a_y = point_a
        b_x, b_y = point_b

        if a_x == b_x: # Vertical line
            self.gradient = "inf"
            self.intercept = 0 if a_x == 0 else None
        else:
            self.gradient = (a_y-b_y)/(a_x-b_x)
            self.intercept = a_y - self.gradient * a_x

    def on_segment(self, a, b, c):
        a_x, a_y = a
        b_x, b_y = b
        c_x, c_y = c

        return min(a_x,b_x) <= c_x <= max(a_x,b_x) and min(a_y,b_y) <= c_y <= max(a_y,b_y)

    def orientation(self, a, b, c):
        a_x, a_y = a
        b_x, b_y = b
        c_x, c_y = c

        val = (b_y - a_y) * (c_x - b_x) - (b_x - a_x) * (c_y - b_y)

        if val == 0: # Colinear
            return 0
        if val > 0: # Clockwise
            return 1 
        return -1 # Counterclockwise

    def intersects(self, other):
        p_a, p_b = self.ends
        p_c, p_d = other.ends

        o1 = self.orientation(p_a, p_b, p_c)
        o2 = self.orientation(p_a, p_b, p_d)
        o3 = self.orientation(p_c, p_d, p_a)
        o4 = self.orientation(p_c, p_d, p_b)

        if o1 != o2 and o3 != o4:
            return True

        if o1 == 0 and self.on_segment(p_a, p_b, p_c): 
            return True
        if o2 == 0 and self.on_segment(p_a, p_b, p_d): 
            return True
        if o3 == 0 and self.on_segment(p_c, p_d, p_a): 
            return True
        if o4 == 0 and self.on_segment(p_c, p_d, p_b): 
            return True

        return False

    # def intersects(self, other):
    #     point_a, point_b = self.ends
    #     point_c, point_d = other.ends

    #     a_x, a_y = point_a
    #     b_x, b_y = point_b
    #     c_x, c_y = point_c
    #     d_x, d_y = point_d

    #     is_common_x_int = (max(a_x,b_x) >= min(c_x,d_x))
    #     is_common_y_int = (max(a_y,b_y) >= min(c_y,d_y))

    #     # If lines are horizontal or parallel, and have common x and y intervals, they intersect
    #     if is_common_x_int and is_common_y_int:
    #         self_vert_or_hor = (self.gradient == 0 or self.gradient == "inf")
    #         other_vert_or_hor = (other.gradient == 0 or other.gradient == "inf")
    #         if self_vert_or_hor or other_vert_or_hor:
    #             return True

    #         if self.gradient == other.gradient:
    #             if self.intercept == other.intercept:
    #                 return True
    #             return False

    #         # Get interval on x-axis where each segment exists
    #         self_x_int = {'min' : min(a_x, b_x), 'max' : max(a_x, b_x)}
    #         other_x_int = {'min' : min(c_x, d_x), 'max' : max(c_x, d_x)}

    #         # Find interval on x-axis where line segments overlap
    #         common_x_int = {'min' : max(self_x_int['min'], other_x_int['min']), 
    #                         'max' : min(self_x_int['max'], other_x_int['max'])}

    #         # Solve simultaneous equation to obtain x intersection point
    #         x_intersect = (self.intercept - other.intercept) / (other.gradient - self.gradient)

    #         if x_intersect >= common_x_int['min'] and x_intersect <= common_x_int['max']:
    #             # x intersect lies on the common x interval of the two segments
    #             # Hence, the line segments intersect
    #             return True
    #     return False

def get_commandos(commando_points, turret_points):
    commandos = []
    for c in commando_points:
        lines = []
        for t in turret_points:
            sight_line = Line_Segment(c,t)
            lines.append(sight_line)
        commando_dict = {'coords' : c, 'sightlines' : lines}
        commandos.append(commando_dict)
    return commandos

def get_base_edges(base_points):
    edges = []
    for i in range(len(base_points)-1):
        edge = Line_Segment(base_points[i], base_points[i+1])
        edges.append(edge)
    edge = Line_Segment(base_points[-1], base_points[0])
    edges.append(edge) # Implicit edge between first and last points
    return edges

def check_intersections(commandos, base_edges):
    safe_commandos = []
    for commando in commandos:
        safe = True
        for line in commando['sightlines']:
            intersects = True in [line.intersects(edge) for edge in base_edges]
            safe = (safe and intersects)
            safe_str = " " if safe else " not "
            print(f"Commando {commando['coords']} is{safe_str}safe")
        if safe:
            safe_commandos.append(commando['coords'])
    return safe_commandos

def simulate(commando_points, turret_points, base_points):
    commandos = get_commandos(commando_points, turret_points)
    base_edges = get_base_edges(base_points)
    return check_intersections(commandos, base_edges)
