import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

transformations = [
    {
        "matrix": np.array([[0.00, 0.00], [0.00, 0.16]]),
        "bias": np.array([0.00, 0.00]),
        "probability": 0.01
    },
    {
        "matrix": np.array([[0.20, -0.26], [0.23, 0.22]]),
        "bias": np.array([0.00, 1.60]),
        "probability": 0.07
    },
    {
        "matrix": np.array([[-0.15, 0.28], [0.26, 0.24]]),
        "bias": np.array([0.00, 0.44]),
        "probability": 0.07
    },
    {
        "matrix": np.array([[0.85, 0.04], [-0.04, 0.85]]),
        "bias": np.array([0.00, 1.60]),
        "probability": 0.85
    }
]
x, y = 0, 0
points = [(x, y)]
num_points = 300000
cumulative_probs = np.cumsum([t["probability"] for t in transformations])
for _ in range(num_points):
    r = np.random.random()
    for i, prob in enumerate(cumulative_probs):
        if r <= prob:
            transform = transformations[i]
            break
    
    point = np.array([x, y])
    new_point = transform["matrix"].dot(point) + transform["bias"]
    x, y = new_point
    
    points.append((x, y))

x_coords, y_coords = zip(*points)

plt.figure(figsize=(6, 10))
plt.scatter(x_coords, y_coords, s=0.1, color='green', alpha=0.5)
plt.title("Leaf Shape")
plt.xlabel("X")
plt.ylabel("Y")
plt.axis('equal')
plt.show()