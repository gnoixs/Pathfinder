import sys
from grid import *
from algorithms.astar import astar
from algorithms.bfs import bfs
from algorithms.dfs import dfs
from algorithms.bidirectional import bidirectional
from algorithms.dijkstras import dijkstras
from algorithms.greedy import greedy

pygame.init()
clock = pygame.time.Clock()
font = pygame.font.Font(None, 25)

WIDTH = 800
HEIGHT = 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pathfinding Visualizer')

ALGORITHMS = [
        ['A*', astar, False],
        ['Breadth-First Search', bfs, False],
        ['Depth-First Search', dfs, False],
        ['Bi-directional A*', bidirectional, False],
        ['Dijkstra\'s', dijkstras, False],
        ['Greedy', greedy, False]
    ]

def main():
    ROWS = 50
    grid = make_grid(ROWS, HEIGHT)

    start = None
    end = None
    selected = None

    run = True
    while run:
        SCREEN.fill(WHITE)
        draw(SCREEN, grid, ROWS, HEIGHT)

        for algorithm in ALGORITHMS:
            i = ALGORITHMS.index(algorithm)
            if algorithm[2] == True:
                pygame.draw.rect(SCREEN, PASTEL_YELLOW, (HEIGHT, (HEIGHT // 8) * i, WIDTH - HEIGHT, (HEIGHT // 8)))
            else:
                pygame.draw.rect(SCREEN, GREY, (HEIGHT, (HEIGHT // 8) * i, WIDTH - HEIGHT, (HEIGHT // 8)))
            text = font.render(algorithm[0], True, BLACK)
            rect = text.get_rect()
            rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 8) * i + (HEIGHT // 16))
            SCREEN.blit(text, rect)
        
        pygame.draw.rect(SCREEN, PASTEL_RED, (HEIGHT, (HEIGHT // 8) * 6, WIDTH - HEIGHT, (HEIGHT // 8)))
        c_text = font.render('Clear', True, BLACK)
        c_rect = c_text.get_rect()
        c_rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 8) * 6 + (HEIGHT // 16))
        SCREEN.blit(c_text, c_rect)

        pygame.draw.rect(SCREEN, PASTEL_GREEN, (HEIGHT, (HEIGHT // 8) * 7, WIDTH - HEIGHT, (HEIGHT // 8)))
        s_text = font.render('Start', True, BLACK)
        s_rect = s_text.get_rect()
        s_rect.center = (HEIGHT + (WIDTH - HEIGHT) / 2, (HEIGHT // 8) * 7 + (HEIGHT // 16))
        SCREEN.blit(s_text, s_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                sys.exit()

            running = False
            if not running:
                if pygame.mouse.get_pressed()[0]:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= HEIGHT:
                        row, col = get_clicked_pos(pos, ROWS, HEIGHT)
                        cell = grid[row][col]
                        if not start and cell != end:
                            start = cell
                            start.make_start()
                        elif not end and cell != start:
                            end = cell
                            end.make_end()
                        elif cell != end and cell != start:
                            cell.make_barrier()
                    else:
                        if 0 <= pos[1] // (HEIGHT // 8) <= 5:
                            if ALGORITHMS[pos[1] // (HEIGHT // 8)][2] == True:
                                ALGORITHMS[pos[1] // (HEIGHT // 8)][2] = False
                                selected = None
                            else:
                                for algorithm in ALGORITHMS:
                                    algorithm[2] = False
                                    selected = None
                                ALGORITHMS[pos[1] // (HEIGHT // 8)][2] = True
                                selected = ALGORITHMS[pos[1] // (HEIGHT // 8)][1]
                        elif pos[1] // (HEIGHT // 8) == 6:
                            start = None
                            end = None
                            grid = make_grid(ROWS, HEIGHT)
                        else:
                            if start and end and selected:
                                running = True
                                for row in grid:
                                    for cell in row:
                                        cell.update_neighbors(grid)
                                        if not cell.is_barrier() and not cell.is_start() and not cell.is_end():
                                            cell.reset()
                                
                                selected(lambda: draw_running(SCREEN, grid, ROWS, HEIGHT), grid, start, end)
                                running = False
                
                if pygame.mouse.get_pressed()[2]:
                    pos = pygame.mouse.get_pos()
                    if pos[0] <= HEIGHT:
                        row, col = get_clicked_pos(pos, ROWS, HEIGHT)
                        cell = grid[row][col]
                        cell.reset()
                        if cell == start:
                            start = None
                        elif cell == end:
                            end = None

        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()