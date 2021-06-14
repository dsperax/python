#estimate pi. Radius = 1
import random

def estimate_pi(n):
    num_dot_in_circle = 0
    num_dot_total = 0
    for _ in range(n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        distance = x**2 + y**2
        if distance <= 1:
            num_dot_in_circle += 1
        num_dot_total += 1
    return 4 * num_dot_in_circle / num_dot_total