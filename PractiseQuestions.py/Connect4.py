# Initialize the 6x7 grid
grid = [['.' for _ in range(7)] for _ in range(6)]

def print_grid():
    for row in grid:
        print(' '.join(row))
    print('1 2 3 4 5 6 7')  # Column numbers

def check_winner(player):
    # Check rows
    for row in range(6):
        for col in range(4):
            if (grid[row][col] == grid[row][col + 1] == grid[row][col + 2] == grid[row][col + 3] == player):
                return True

    # Check columns
    for col in range(7):
        for row in range(3):
            if (grid[row][col] == grid[row + 1][col] == grid[row + 2][col] == grid[row + 3][col] == player):
                return True

    # Check diagonals (positive slope)
    for row in range(3):
        for col in range(4):
            if (grid[row][col] == grid[row + 1][col + 1] == grid[row + 2][col + 2] == grid[row + 3][col + 3] == player):
                return True

    # Check diagonals (negative slope)
    for row in range(3, 6):
        for col in range(4):
            if (grid[row][col] == grid[row - 1][col + 1] == grid[row - 2][col + 2] == grid[row - 3][col + 3] == player):
                return True

    return False

def drop_piece(col, player):
    for row in range(5, -1, -1):
        if grid[row][col] == '.':
            grid[row][col] = player
            break

print("Welcome to Connect Four!")
print_grid()

player = 'x'
while True:
    try:
        col = int(input(f"Player {player}, select a column (1-7): ")) - 1
        if col < 0 or col > 6 or grid[0][col] != '.':
            print("Invalid move! Try again.")
            continue
        
        drop_piece(col, player)
        print_grid()

        if check_winner(player):
            print(f"Player {player} wins!")
            break

        # Switch player
        player = 'o' if player == 'x' else 'x'

    except ValueError:
        print("Invalid input! Enter a number.")
