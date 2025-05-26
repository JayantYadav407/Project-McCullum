import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import time

# Simulation parameters
plate_size = 1.0
num_particles = 1000
base_frequency = 50
frequency_increment = 50
num_modes = 6
damping_factor = 0.02
environmental_noise = 0.002
excitation_point = (0.5, 0.5)
max_frequency = 500

def wave_function(x, y, modes, excitation_point, plate_size):
    nx, ny = modes
    ex, ey = excitation_point
    excitation_effect = np.exp(-((x - ex) ** 2 + (y - ey) ** 2) * 15)
    return np.sin(nx * np.pi * x / plate_size) * np.sin(ny * np.pi * y / plate_size) * excitation_effect

def simulate_chladni_plate(frequency, num_particles, num_modes):
    particles = np.random.rand(num_particles, 2) * plate_size
    grid_points = 500
    x = np.linspace(0, plate_size, grid_points)
    y = np.linspace(0, plate_size, grid_points)
    X, Y = np.meshgrid(x, y)
    modes = [(nx, ny) for nx in range(1, num_modes + 1) for ny in range(1, num_modes + 1)]
    pattern = np.zeros_like(X)

    for mode in modes:
        mode_freq = (np.sqrt(mode[0]**2 + mode[1]**2)) / (2 * plate_size)
        weight = np.exp(-((frequency - mode_freq) / (0.1 * frequency))**2)
        pattern += weight * wave_function(X, Y, mode, excitation_point, plate_size)

    pattern *= np.sin(2 * np.pi * frequency * 0.001)
    pattern /= np.max(np.abs(pattern))
    scale = grid_points / plate_size

    for _ in range(200):
        idx = (particles * scale).astype(int)
        idx = np.clip(idx, 0, grid_points - 1)
        displacement = pattern[idx[:, 0], idx[:, 1]]
        noise = np.random.normal(0, environmental_noise, size=(num_particles, 2))
        movement = (-0.02 * displacement[:, np.newaxis] + noise) * (1 - damping_factor)
        particles += movement
        particles = np.clip(particles, 0, plate_size)

    return particles

# Create animation
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, plate_size)
ax.set_ylim(0, plate_size)
ax.set_facecolor('white')
particles_plot, = ax.plot([], [], 'ko', markersize=1)

def init():
    particles_plot.set_data([], [])
    return particles_plot,

def update(frame):
    frequency = base_frequency + frame * frequency_increment
    particles = simulate_chladni_plate(frequency, num_particles, num_modes)
    particles_plot.set_data(particles[:, 0], particles[:, 1])
    ax.set_title(f"Frequency: {frequency} Hz", color='black')
    
    # Pause for 5 seconds every 50 Hz increment
    if frame > 0 and frame % 50 == 0:
        time.sleep(5)
    
    return particles_plot,

num_frames = (max_frequency - base_frequency) // frequency_increment
ani = FuncAnimation(fig, update, frames=num_frames, init_func=init, blit=True, interval=5)
plt.show()
