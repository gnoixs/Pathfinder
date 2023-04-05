from queue import Queue

from algorithms.helpers import make_path

# Define BFS
def bfs(draw, grid, start, end):
    # Initialize queue with start
    q = Queue()
    q.put(start)

    # Initialize dictionary to keep track of visited and previous
    visited = {start}
    previous = {}

    # Loop until q is empty
    while not q.empty():
        # Get current
        current = q.get()

        # If current is end, make path and return True
        if current == end:
            make_path(previous, end, draw)
            end.make_end()
            start.make_start()
            return True
        
        # Loop through neighbors of current
        for neighbor in current.neighbors:
            # If neighbor has not been visited and is not barrier, add to q, mark visited, update previous, and mark open
            if neighbor not in visited and not neighbor.is_barrier():
                q.put(neighbor)
                visited.add(neighbor)
                previous[neighbor] = current
                neighbor.make_open()

        draw()

        # If current is not start, mark it as closed
        if current != start:
            current.make_closed()

    # If end is not found, return False
    return False