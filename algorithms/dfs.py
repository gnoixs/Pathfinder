def make_path(previous, current, draw):
    count = 0
    while current in previous and count != len(previous):
        current = previous[current]
        current.make_path()
        draw()
        count += 1

def dfs(draw, grid, start, end):
    # Initialize stack with start
    s = [start]

    # Initialize dictionary to keep track of visited and previous
    visited = set()
    previous = {}

    # Loop until s is empty
    while len(s) != 0:
        # Get current
        current = s.pop()

        # If current is end, return True
        if current == end:
            print('making path')
            make_path(previous, end, draw)
            print('exiting path')
            end.make_end()
            start.make_start()
            return True
    
        # Loop through neighbors of current
        for neighbors in current.neighbors:
            # If neighbor has not been visited and is not barrier, add to s, mark visited, update previous, and mark open
            if neighbors not in visited and not neighbors.is_barrier():
                s.append(neighbors)
                visited.add(neighbors)
                previous[neighbors] = current
                neighbors.make_open()

        draw()

        # If current is not start, mark it as closed
        if current != start:
            current.make_closed()
    
    print('loop terminated')
    # If end is not found, return False
    return False