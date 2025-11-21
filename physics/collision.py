
def is_colliding(a, b):
    return (
        a.x < b.x + b.size and
        a.x + a.size > b.x and
        a.y < b.y + b.size and
        a.y + a.size > b.y
    )
    
def resolve_collision(a, b, e):
    ax_left = a.x
    ax_right = a.x + a.size
    ay_top = a.y + a.size #TODO: check if its correct. if theres a bug, suppose its because of this
    ay_bottom = a.y
    bx_left = b.x
    bx_right = b.x + b.size
    by_top = b.y + b.size #TODO: check if its correct. if theres a bug, suppose its because of this
    by_bottom = b.y
    ax_center = a.x + a.size / 2
    ay_center = a.y + a.size / 2
    bx_center = b.x + b.size / 2
    by_center = b.y + b.size / 2
    overlap_x1 = ax_right - bx_left
    overlap_x2 = bx_right - ax_left
    overlap_x = min(overlap_x1, overlap_x2)
    overlap_y1 = ay_top - by_bottom
    overlap_y2 = by_top - ay_bottom
    overlap_y = min(overlap_y1, overlap_y2)
    
    u_a_x = a.vx
    u_b_x = b.vx
    u_a_y = a.vy
    u_b_y = b.vy
    mass_a = a.mass
    mass_b = b.mass
    
    if overlap_x < overlap_y:
        if ax_center < bx_center:
            a.x -= overlap_x
        else:
            a.x += overlap_x

        a.vx = ((mass_a * u_a_x + mass_b * u_b_x) - mass_b * (u_a_x - u_b_x)*e)/(mass_a + mass_b) 
        b.vx = ((mass_a * u_a_x + mass_b * u_b_x) + mass_a * (u_a_x - u_b_x)*e)/(mass_a + mass_b)
    else:
        if ay_center < by_center:
            a.y -= overlap_y
        else:
            a.y += overlap_y

        a.vy = ((mass_a * u_a_y + mass_b * u_b_y) - mass_b * (u_a_y - u_b_y)*e)/(mass_a + mass_b) 
        b.vy = ((mass_a * u_a_y + mass_b * u_b_y) + mass_a * (u_a_y - u_b_y)*e)/(mass_a + mass_b)