def calculate_gravitational_force(m1, m2, d):
    G = 6.674 * (10**-11)
    force = G * (m1 * m2) / (d**2)
    return force