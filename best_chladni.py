import numpy as np
import matplotlib.pyplot as plt

# Simulation parameters
plate_size = 1.0  # Plate size (1m x 1m)
num_particles = 10000  # Number of particles
frequency = 285  # Initial frequency in Hz (can sweep or remain fixed)
c = 343  # Speed of sound in m/s (approximate for steel)
damping_factor = 0.01  # Damping effect
excitation_point = (0.5, 0.5)  # Excitation point at the center of the plate
particle_mass = 0.01  # Mass of each particle (in kg), adjusts response behavior
environmental_resistance = 0.05  # Simulate air resistance

def wave_function(x, y, modes, excitation_point):
    """
    Calculate the standing wave pattern on the plate considering excitation point.

    Args:
        x (ndarray): x-coordinates.
        y (ndarray): y-coordinates.
        modes (tuple): Modes of vibration (nx, ny).
        excitation_point (tuple): Location of excitation force.

    Returns:
        ndarray: Displacement values at (x, y).
    """
    nx, ny = modes
    ex, ey = excitation_point
    excitation_effect = np.exp(-((x - ex) ** 2 + (y - ey) ** 2) * 10)  # Effect decreases with distance
    return np.sin(nx * np.pi * x / plate_size) * np.sin(ny * np.pi * y / plate_size) * excitation_effect

def simulate_chladni_plate(frequency, num_particles, num_modes=5):
    """
    Simulate Chladni plate patterns and particle movement.

    Args:
        frequency (float): Frequency of vibration.
        num_particles (int): Number of particles.
        num_modes (int): Number of modes to superimpose.

    Returns:
        ndarray: Final positions of the particles.
    """
    # Generate random initial positions for particles
    particles = np.random.rand(num_particles, 2) * plate_size

    # Superpose multiple modes
    modes = [(nx, ny) for nx in range(1, num_modes + 1) for ny in range(1, num_modes + 1)]

    # Calculate vibration pattern
    x = np.linspace(0, plate_size, 500)
    y = np.linspace(0, plate_size, 500)
    X, Y = np.meshgrid(x, y)
    pattern = np.zeros_like(X)
    for mode in modes:
        pattern += wave_function(X, Y, mode, excitation_point)

    # Adjust pattern intensity based on frequency
    pattern *= np.sin(2 * np.pi * frequency * 0.001)  # Simulating temporal effect of frequency

    # Normalize the pattern
    pattern /= np.max(np.abs(pattern))

    # Move particles toward nodal lines
    for _ in range(500):  # Iterations for particle movement
        for i, (px, py) in enumerate(particles):
            # Get nearest grid point
            ix = int(px / plate_size * (X.shape[0] - 1))
            iy = int(py / plate_size * (Y.shape[1] - 1))

            # Calculate displacement at particle's position
            displacement = pattern[ix, iy]

            # Move particle based on displacement, damping, and environmental resistance
            particles[i] += (-0.01 * displacement / particle_mass * np.array([
                np.sign(px - X[ix, iy]),
                np.sign(py - Y[ix, iy])
            ])) * (1 - damping_factor) * (1 - environmental_resistance)

        # Keep particles within plate boundaries
        particles = np.clip(particles, 0, plate_size)

    return particles

def plot_chladni_pattern(particles, frequency, num_particles, c, damping_factor):
    """
    Plot the Chladni plate pattern.

    Args:
        particles (ndarray): Particle positions.
        frequency (float): Frequency used for the pattern.
        num_particles (int): Number of particles used.
        c (float): Speed of sound.
        damping_factor (float): Damping factor used.
    """
    plt.figure(figsize=(8, 8))
    plt.scatter(particles[:, 0], particles[:, 1], s=1, color='black', alpha=0.5)
    plt.xlim(0, plate_size)
    plt.ylim(0, plate_size)
    plt.axis('off')
    plt.title(f"Chladni Pattern (Freq: {frequency} Hz, Particles: {num_particles}, c: {c:.2f} m/s, Damping: {damping_factor})")
    plt.show()

# Run simulation
particles = simulate_chladni_plate(frequency, num_particles)
plot_chladni_pattern(particles, frequency, num_particles, c, damping_factor)
