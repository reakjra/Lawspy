import math

def calculate_refraction_angle(incident_angle, refractive_index1, refractive_index2):
    refraction_angle = math.asin((refractive_index1 / refractive_index2) * math.sin(math.radians(incident_angle)))
    return math.degrees(refraction_angle)