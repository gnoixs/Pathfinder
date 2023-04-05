from math import dist

# Heuristic function to estimate distance between two points
def h(p1, p2):
    return dist(p1, p2) # Euclidean

# Function to make path from start to end by backtracking
def make_path(previous, current, draw):
    while current in previous:
        current = previous[current]
        current.make_path()
        draw()