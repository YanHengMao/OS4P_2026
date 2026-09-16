ACCELERATION_G = 9.80665  # m/s^2
TIME = 5.0  # seconds


def calculate_displacement(g, t):
    return 0.5 * g * t**2


displacement = calculate_displacement(ACCELERATION_G, TIME)
print(f"Displacement: {displacement} meters")
