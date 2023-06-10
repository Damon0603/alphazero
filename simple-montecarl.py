import random

def estimate_pi(num_samples):
    num_points_in_circle = 0

    for _ in range(num_samples):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        distance = x**2 + y**2
        if distance <= 1:
            num_points_in_circle += 1

    pi_estimate = 4 * (num_points_in_circle / num_samples)
    return pi_estimate

# Anzahl der Simulationen
num_simulations = 100000

# Schätzung von Pi
pi_estimate = estimate_pi(num_simulations)
print("Pi-Schätzung:", pi_estimate)


estimate_pi(1000000)

