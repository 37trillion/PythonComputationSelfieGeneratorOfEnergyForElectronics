import time
import random

# Constants
particle_mass = 1.0  # Mass of the particle (for simulation)
initial_velocity = 0.0  # Initial velocity of the particle
sound_intensity = 1.0  # Intensity of the sound (arbitrary unit)
frequency = 440.0  # Frequency of the sound wave (in Hz)

# Simulation parameters
simulation_duration = 10  # Duration of the simulation (seconds)
time_step = 0.01  # Time step for simulation (seconds)

# Function to calculate force based on sound intensity and particle mass
def calculate_force(sound_intensity, particle_mass):
    # In this simplified model, force is proportional to sound intensity
    return sound_intensity * particle_mass

# Initialize particle properties
position = 0.0
velocity = initial_velocity

# Simulation loop
for t in range(int(simulation_duration / time_step)):
    # Generate a random sound intensity (for simplicity)
    sound_intensity = random.uniform(0.0, 1.0)

    force = calculate_force(sound_intensity, particle_mass)
    acceleration = force / particle_mass
    velocity += acceleration * time_step
    position += velocity * time_step

    # Print the position of the particle and sound intensity at each time step
    print(f"Time: {t * time_step:.2f}s, Position: {position:.2f}m, Sound Intensity: {sound_intensity:.2f}")

    # Sleep to simulate real-time behavior
    time.sleep(time_step)

print("Simulation complete!")