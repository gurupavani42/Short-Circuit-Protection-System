# Short-Circuit Protection System
# EEE Python Mini Project

# Protection limits
MAX_CURRENT = 100       # Maximum safe current (A)
MIN_IMPEDANCE = 1.0     # Minimum safe impedance (Ohm)


def short_circuit_protection(voltage, current, impedance):

    print("\n======================================")
    print("    SHORT-CIRCUIT PROTECTION SYSTEM")
    print("======================================")

    print(f"Voltage   : {voltage:.2f} V")
    print(f"Current   : {current:.2f} A")
    print(f"Impedance : {impedance:.2f} Ohm")

    fault = False

    # Check for excessive current
    if current > MAX_CURRENT:
        print("\n⚠ OVER-CURRENT DETECTED")
        fault = True

    # Check for very low impedance
    if impedance < MIN_IMPEDANCE:
        print("⚠ LOW IMPEDANCE DETECTED")
        fault = True

    # Protection decision
    print("\n----------- PROTECTION STATUS -----------")

    if fault:
        print("⚠ SHORT-CIRCUIT FAULT DETECTED")
        print("Protection Status : TRIP")
        print("Circuit Breaker   : OFF")
        print("Load Supply       : DISCONNECTED")

    else:
        print("✓ SYSTEM NORMAL")
        print("Protection Status : NORMAL")
        print("Circuit Breaker   : ON")
        print("Load Supply       : CONNECTED")


# Main program

print("======================================")
print("       SHORT-CIRCUIT MONITOR")
print("======================================")

voltage = float(input("Enter Voltage (V): "))
current = float(input("Enter Current (A): "))
impedance = float(input("Enter Circuit Impedance (Ohm): "))

short_circuit_protection(
    voltage,
    current,
    impedance
)
