import heapq

from algorithms.helpers import make_path

def h(point1, point2):
    return abs(point1.row - point2.row) + abs(point1.col - point2.col)

def greedy(draw, grid, start, end):
    # Using a heap instead of a queue to prioritize exploring nodes with lowest estimated distance to the end point
    heap = []
    heapq.heappush(heap, (0, start))

    # Using a set to keep track of visited nodes
    visited = {start}
    came_from = {}

    while heap:

        # Get the node with the lowest estimated distance to the end point
        current = heapq.heappop(heap)[1]

        if current == end:
            make_path(came_from, end, draw)
            end.make_end()
            start.make_start()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited and not neighbor.is_barrier():
                heapq.heappush(heap, (h(neighbor, end), neighbor))
                visited.add(neighbor)
                came_from[neighbor] = current
                neighbor.make_open()

        draw()

        if current != start:
            current.make_closed()

    return False