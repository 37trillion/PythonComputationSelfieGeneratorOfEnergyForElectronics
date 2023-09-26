from flask import Flask, render_template, request, jsonify
import time
import random

app = Flask(__name__)

# Constants
initial_energy = 1000.0  # Initial energy (arbitrary unit)
energy_loss_rate = 0.1   # Rate of energy loss per second
particle_energy_conversion = 0.05  # Energy converted into particles per second

# Initialize energy and particle count
energy = initial_energy
particle_count = 0

# Function to simulate energy generation
def generate_energy():
    global energy, particle_count
    energy -= energy_loss_rate
    particle_count += energy * particle_energy_conversion

# Function to simulate particle generation
def generate_particles():
    global particle_count
    particle_count += 10  # Arbitrary particle generation rate

@app.route("/", methods=["GET", "POST"])
def index():
    global energy, particle_count

    if request.method == "POST":
        action = request.form["action"]
        if action == "generate_energy":
            generate_energy()
        elif action == "generate_particles":
            generate_particles()

    return render_template("index.html", energy=energy, particle_count=particle_count)

@app.route("/api/status", methods=["GET"])
def get_status():
    return jsonify({"energy": energy, "particle_count": particle_count})

if __name__ == "__main__":
    app.run(debug=True)
