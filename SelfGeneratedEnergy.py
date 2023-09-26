import time

# Constants
particle_mass = 1.0  # Mass of the particle (for simulation)
initial_velocity = 0.0  # Initial velocity of the particle
frequency = 1.0  # Frequency of the emitted signal (Hz)

# Simulation parameters
simulation_duration = 10  # Duration of the simulation (seconds)
time_step = 0.01  # Time step for simulation (seconds)

# Function to calculate force based on frequency and particle mass
def calculate_force(frequency, particle_mass):
    angular_frequency = 2 * 3.14159 * frequency
    return angular_frequency ** 2 * particle_mass

# Initialize particle properties
position = 0.0
velocity = initial_velocity

# Simulation loop
for t in range(int(simulation_duration / time_step)):
    force = calculate_force(frequency, particle_mass)
    acceleration = force / particle_mass
    velocity += acceleration * time_step
    position += velocity * time_step

    # Print the position of the particle at each time step
    print(f"Time: {t * time_step:.2f}s, Position: {position:.2f}m")

    # Sleep to simulate real-time behavior
    time.sleep(time_step)

print("Simulation complete!")