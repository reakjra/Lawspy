def calculate_voltage(current, resistance):
    voltage = current * resistance
    return voltage

def calculate_current(voltage, resistance):
    current = voltage / resistance
    return current

def calculate_resistance(voltage, current):
    resistance = voltage / current
    return resistance