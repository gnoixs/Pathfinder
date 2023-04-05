from cell import *

def make_grid(rows, width):
	grid = []
	gap = width // rows
	for i in range(rows):
		grid.append([])
		for j in range(rows):
			cell = Cell(i, j, gap, rows)
			grid[i].append(cell)

	return grid


def draw_grid(win, rows, width):
	gap = width // rows
	for i in range(rows):
		pygame.draw.line(win, GREY, (0, i * gap), (width, i * gap))
		for j in range(rows + 1):
			pygame.draw.line(win, GREY, (j * gap, 0), (j * gap, width))


def draw(win, grid, rows, width):
	for row in grid:
		for cell in row:
			cell.draw(win)
	draw_grid(win, rows, width)

def draw_running(win, grid, rows, width):
	for row in grid:
		for cell in row:
			cell.draw(win)
	draw_grid(win, rows, width)
	pygame.display.update()

def get_clicked_pos(pos, rows, height):
    gap = height // rows
    y, x = pos

    row = y // gap
    col = x // gap

    return row, col