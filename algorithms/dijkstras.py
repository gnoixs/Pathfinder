from queue import PriorityQueue

from algorithms.helpers import make_path

# Define Dijkstras
def dijkstras(draw, grid, start, end):
    count = 0

    # Initialize priority queue with start
    pq = PriorityQueue()
    pq.put((0, count, start))

    # Initialize dictionary to keep track of previous
    previous = {}

    # Initialize dictionary to keep track of g
    g = {cell: float("inf") for row in grid for cell in row}
    g[start] = 0
    
    # Loop until pq is empty
    while not pq.empty():
        # get lowest g
        current = pq.get()[2]
        
        # If current is end, make path and return True
        if current == end:
            make_path(previous, end, draw)
            end.make_end()
            start.make_start()
            return True

        # Loop through neighbors of current
        for neighbor in current.neighbors:
            # Calculate tentative g
            temp_g = g[current] + 1

            # If tentative g is less than current g, update g and previous
            if temp_g < g[neighbor]:
                previous[neighbor] = current
                g[neighbor] = temp_g
                # If neighbor is not in set, add it to pq and set
                if neighbor not in [item[2] for item in pq.queue]:
                    count += 1
                    pq.put((g[neighbor], count, neighbor))
                    neighbor.make_open()

        draw()

        # If current is not start, mark it as closed
        if current != start:
            current.make_closed()

    # If end is not found, return False
    return False