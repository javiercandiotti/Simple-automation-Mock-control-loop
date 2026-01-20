import time

# Fake battery parameters
battery_capacity_wh = 100.0      # Wh
current_soc = 20.0               # State of Charge (%)
charge_rate_w = 50.0             # Watts
discharge_rate_w = 80.0
max_voltage = 4.2
min_voltage = 3.0

print("Starting mock battery control loop...\n")

for step in range(1, 21):
    # Decide action
    if current_soc < 30:
        action = "CHARGING"
        power = charge_rate_w
        delta_soc = (power / battery_capacity_wh) * 100 * 0.1  # 0.1 = 6 min step
    elif current_soc > 80:
        action = "DISCHARGING"
        power = -discharge_rate_w
        delta_soc = (power / battery_capacity_wh) * 100 * 0.1
    else:
        action = "IDLE"
        power = 0
        delta_soc = 0

    # Update SOC
    current_soc += delta_soc
    current_soc = max(0, min(100, current_soc))  # Keep between 0–100%

    # Fake voltage (very simplified)
    voltage = min_voltage + (max_voltage - min_voltage) * (current_soc / 100)

    print(f"Step {step:2d} | SOC: {current_soc:5.1f}% | Voltage: {voltage:.3f}V | Action: {action:12} | Power: {power:+.1f}W")

    time.sleep(0.5)  # Just to make it feel real-time

print("\nSimulation finished.")