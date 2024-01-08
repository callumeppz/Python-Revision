import random
import copy

# Function to count live neighbors for a given cell
def count_live_neighbors(grid, x, y):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if (x + i >= 0 and x + i < len(grid)) and (y + j >= 0 and y + j < len(grid[0])):
                count += grid[x + i][y + j]
    count -= grid[x][y]
    return count

# Function to perform one iteration of the Game of Life
def game_of_life(grid):
    new_grid = copy.deepcopy(grid)  # Create a new grid to store the updated values

    # Iterate through each cell in the grid
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            live_neighbors = count_live_neighbors(grid, i, j)

            # Apply the rules of the game
            if grid[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                new_grid[i][j] = 0  # Cell dies due to underpopulation or overcrowding
            elif grid[i][j] == 0 and live_neighbors == 3:
                new_grid[i][j] = 1  # Cell comes to life due to exactly 3 live neighbors

    return new_grid

# Define the grid size
rows, cols = 10, 10

# Create a random initial grid with zeros and ones (dead and alive cells)
initial_grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]

# Perform one iteration of the game
new_iteration = game_of_life(initial_grid)

# Display the original and updated grids
print("Original Grid:")
for row in initial_grid:
    print(' '.join(map(str, row)))

print("\nNext Iteration:")
for row in new_iteration:
    print(' '.join(map(str, row)))
