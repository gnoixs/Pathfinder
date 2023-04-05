from queue import PriorityQueue

from algorithms.helpers import h

def make_path(previous_start, previous_end, middle, draw):
    path = []
    current = middle
    
    # Find path from start to middle
    while current in previous_start:
        path.append(current)
        current = previous_start[current]
    
    # Reverse path and find path from middle to end
    path = path[::-1]
    current = previous_end[middle]
    
    while current in previous_end:
        path.append(current)
        current = previous_end[current]
    
    # Make cells in path as part of path and draw
    for cell in path:
        cell.make_path()
        draw()

# Define Bi-Directional A*
def bidirectional(draw, grid, start, end):
    count = 0

    # Initialization of priority queues
    pq_start = PriorityQueue()
    pq_start.put((0, count, start))
    previous_start = {start: None}
    g_start = {cell: float("inf") for row in grid for cell in row}
    g_start[start] = 0
    f_start = {cell: float("inf") for row in grid for cell in row}
    f_start[start] = h(start.get_pos(), end.get_pos())
    pq_hash_start = {start}

    pq_end = PriorityQueue()
    pq_end.put((0, count, end))
    previous_end = {end: None}
    g_end = {cell: float("inf") for row in grid for cell in row}
    g_end[end] = 0
    f_end = {cell: float("inf") for row in grid for cell in row}
    f_end[end] = h(start.get_pos(), end.get_pos())
    pq_hash_end = {end}

    middle = None

    # Loop until pqs are empty
    while not pq_start.empty() and not pq_end.empty():

        # get lowest f and remove
        current_start = pq_start.get()[2]
        pq_hash_start.remove(current_start)

        current_end = pq_end.get()[2]
        pq_hash_end.remove(current_end)

        # If current is end, break
        if current_start in pq_hash_end:
            middle = current_start
            break

        if current_end in pq_hash_end:
            middle = current_end
            break

        # Loop through current neighbors
        for neighbor in current_start.neighbors:
            temp_g_score = g_start[current_start] + 1

            if temp_g_score < g_start[neighbor]:
                previous_start[neighbor] = current_start
                g_start[neighbor] = temp_g_score
                f_start[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in pq_hash_start:
                    count += 1
                    pq_start.put((f_start[neighbor], count, neighbor))
                    pq_hash_start.add(neighbor)
                    neighbor.make_open()

        for neighbor in current_end.neighbors:
            temp_g_score = g_end[current_end] + 1

            if temp_g_score < g_end[neighbor]:
                previous_end[neighbor] = current_end
                g_end[neighbor] = temp_g_score
                f_end[neighbor] = temp_g_score + h(neighbor.get_pos(), end.get_pos())
                if neighbor not in pq_hash_end:
                    count += 1
                    pq_end.put((f_end[neighbor], count, neighbor))
                    pq_hash_end.add(neighbor)
                    neighbor.make_open()

        draw()

        # If current is not start, mark it as closed
        if current_start != start:
            current_start.make_closed()

        if current_end != end:
            current_end.make_closed()
    
    # Make path and return True
    if middle is not None:
        make_path(previous_start, previous_end, middle, draw)
        start.make_start()
        end.make_end()
        return True
    
    # If end is not found, return False
    return False