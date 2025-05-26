import numpy as np
import matplotlib.pyplot as plt
import random
import time
import sys

# For Windows non-blocking input
try:
    import msvcrt
    def timed_input(prompt, timeout=6):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        end_time = time.time() + timeout
        buf = ''
        while time.time() < end_time:
            if msvcrt.kbhit():
                ch = msvcrt.getwch()
                if ch in ['\r', '\n']:
                    sys.stdout.write('\n')
                    return buf
                sys.stdout.write(ch)
                sys.stdout.flush()
                buf += ch
            time.sleep(0.01)
        sys.stdout.write('\n')
        return None
except ImportError:
    # Fallback for Unix-like
    import select
    def timed_input(prompt, timeout=6):
        sys.stdout.write(prompt)
        sys.stdout.flush()
        ready, _, _ = select.select([sys.stdin], [], [], timeout)
        if ready:
            line = sys.stdin.readline().rstrip('\n')
            return line
        sys.stdout.write('\n')
        return None

# Physical properties of plate
E = 2.0e11          # Young's modulus (Pa)
rho = 7800          # Density (kg/m^3)
thickness = 0.005   # Thickness (m)
plate_size = 1.0    # Plate size (m)
c = np.sqrt(E / rho)  # Wave speed in plate material (m/s)

# Environmental air properties
air_temp = 20       # Celsius
air_pressure = 101325  # Pa
c_air = 331 + 0.6 * air_temp  # Approximate sound speed in air (m/s)

# Simulation parameters
base_frequency = 285  # Hz
num_particles = 10000
damping_factor = 0.02     # Damping due to material and air friction
environmental_noise = 0.002 # External vibrations/noise intensity
excitation_point = (0.5, 0.5)  # Center excitation

# Wave function definition
def wave_function(x, y, modes, excitation_point, plate_size):
    nx, ny = modes
    ex, ey = excitation_point
    excitation_effect = np.exp(-((x - ex) ** 2 + (y - ey) ** 2) * 15)
    return np.sin(nx * np.pi * x / plate_size) * np.sin(ny * np.pi * y / plate_size) * excitation_effect

# Simulation routine
def simulate_chladni_plate(frequency, num_particles, num_modes=6):
    particles = np.random.rand(num_particles, 2) * plate_size
    grid_points = 500
    x = np.linspace(0, plate_size, grid_points)
    y = np.linspace(0, plate_size, grid_points)
    X, Y = np.meshgrid(x, y)
    modes = [(nx, ny) for nx in range(1, num_modes + 1) for ny in range(1, num_modes + 1)]
    pattern = np.zeros_like(X)
    for mode in modes:
        mode_freq = c * np.sqrt(mode[0]**2 + mode[1]**2) / (2 * plate_size)
        weight = np.exp(-((frequency - mode_freq) / (0.1 * frequency))**2)
        pattern += weight * wave_function(X, Y, mode, excitation_point, plate_size)
    pattern *= np.sin(2 * np.pi * frequency * 0.001)
    pattern /= np.max(np.abs(pattern))
    scale = grid_points / plate_size
    for _ in range(300):
        idx = (particles * scale).astype(int)
        idx = np.clip(idx, 0, grid_points - 1)
        displacement = pattern[idx[:,0], idx[:,1]]
        noise = np.random.normal(0, environmental_noise, size=(num_particles, 2))
        movement = (-0.02 * displacement[:, np.newaxis] + noise) * (1 - damping_factor)
        particles += movement
        particles = np.clip(particles, 0, plate_size)
    return particles, pattern

# Plotting routine
def plot_chladni_pattern(particles, frequency):
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_facecolor('#121212')  # pencil black background
    ax.scatter(particles[:, 0], particles[:, 1], s=1, c='black', alpha=0.85)
    ax.axis('off')
    ax.set_title(f"Chladni Plate Pattern - Frequency: {frequency:.1f} Hz", color='white')
    plt.show(block=False)
    plt.pause(2)
    plt.close(fig)

# Main loop with timed input
while True:
    user_input = timed_input("Enter frequency factor (1-1000, 0 to quit) [auto-random in 1s]: ", timeout=1)
    if user_input is None:
        freq_factor = random.randint(1,100)
        print(f"Auto-selected factor: {freq_factor}")
    else:
        try:
            freq_factor = float(user_input)
        except ValueError:
            print("Invalid input; try again.")
            continue
    if freq_factor == 0:
        break
    frequency = base_frequency * freq_factor
    particles, _ = simulate_chladni_plate(frequency, num_particles)
    plot_chladni_pattern(particles, frequency)
