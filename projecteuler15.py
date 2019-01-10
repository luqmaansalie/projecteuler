
# https://projecteuler.net/problem=15

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

# 2, 6, 20, 

# 4, 12, 24, 40, 60

# |_|

# |_|_|
# |_|_|

# |_|_|_|
# |_|_|_|
# |_|_|_|

# |_|_|_|_|
# |_|_|_|_|
# |_|_|_|_|
# |_|_|_|_|

# |_|_|_|_|_|
# |_|_|_|_|_|
# |_|_|_|_|_|
# |_|_|_|_|_|
# |_|_|_|_|_|



gridSize = 0
grid = [0] * (gridSize+1)
grid = [grid] * (gridSize+1)

for i in range(gridSize):
	grid[i][gridSize] = 1
	grid[gridSize][i] = 1

for i in range(gridSize -1 , -1, -1):
	for j in range(gridSize -1 , -1, -1):
		grid[i][j] = grid[i+1][j] + grid[i][j+1]

print(grid[0][0])

routes = {}

def calcRoutes(x, y):
	if x == 0 or y == 0:
		return 1
	
	xy = (x, y)
	if xy in routes:
		return routes[xy]
	
	routes[xy] = calcRoutes(x-1, y) + calcRoutes(x, y-1)
	return routes[xy]

print(calcRoutes(20, 20))
