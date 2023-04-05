from queue import PriorityQueue
from algorithms.helpers import *

# Define A*
def astar(draw, grid, start, end):
	count = 0

    # Initialize priority queue with start
	pq = PriorityQueue()
	pq.put((0, count, start))

    # Initialize dictionary to keep track of previous
	previous = {}

    # Initialize dictionaries to keep track of g and f
	g = {cell: float("inf") for row in grid for cell in row}
	g[start] = 0
	f = {cell: float("inf") for row in grid for cell in row}
	f[start] = h(start.get_pos(), end.get_pos())

    # Initialize set to keep track of nodes in pq
	pq_hash = {start}

    # Loop until pq is empty
	while not pq.empty():
        # Get node with lowest f and remove
		current = pq.get()[2]
		pq_hash.remove(current)

        # If current is end, make path and return True
		if current == end:
			make_path(previous, end, draw)
			end.make_end()
			return True

        # Loop through neighbors of current
		for neighbor in current.neighbors:
			# Calculate tentative g
			temp_g = g[current] + 1

            # If tentative g is less than current g, update g and previous
			if temp_g < g[neighbor]:
				previous[neighbor] = current
				g[neighbor] = temp_g
				f[neighbor] = temp_g + h(neighbor.get_pos(), end.get_pos())
                # If neighbor is not in set, add it to pq and set
				if neighbor not in pq_hash:
					count += 1
					pq.put((f[neighbor], count, neighbor))
					pq_hash.add(neighbor)
					neighbor.make_open()

		draw()

        # If current is not start, mark it as closed
		if current != start:
			current.make_closed()
            
    # If end is not found, return False
	return False