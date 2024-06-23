from math import gcd

def triangle_area(p1, p2, q1, q2, r1, r2):
    return abs(p1 * (q2 - r2) + q1 * (r2 - p2) + r1 * (p2 - q2))

def boundary_lattice_points(p1, p2, q1, q2):
    return gcd(abs(p1 - q1), abs(p2 - q2))

def interior_lattice_points(p, q, r):
    p1, p2 = p
    q1, q2 = q
    r1, r2 = r
    
    # Calculate the area of the triangle
    area = triangle_area(p1, p2, q1, q2, r1, r2)
    
    # Calculate the number of lattice points on the boundary
    B = (boundary_lattice_points(p1, p2, q1, q2) +
         boundary_lattice_points(q1, q2, r1, r2) +
         boundary_lattice_points(r1, r2, p1, p2))
    
    # Calculate the number of interior lattice points using Pick's Theorem
    I = (area - B + 2) // 2
    
    return int(I)

# Test cases
print(interior_lattice_points((0, 0), (0, 5), (5, 0)))  # Output: 6
print(interior_lattice_points((62, -3), (5, -45), (-19, -23)))  # Output: 1129

# Custom test case
p = (12033669, 485659567)
q = (348638641, 745372627)
r = (795130940, 558994116)
print(interior_lattice_points(p, q, r))  # Expected Output: 89347907358140809
