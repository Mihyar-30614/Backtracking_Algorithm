import sys
# Helper function to print Grid
def print_grid(grid):
    print("")
    for i in range(9):
        line = ''
        for j in range(9):
            line += str(grid[i][j]) + " "
        print(line)

# Helper function to locate empty locations
def find_empty_location(grid, empty_list):
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                empty_list[0] = row
                empty_list[1] = col
                return True
    return False

# Helper function to check if digit exists in row
def used_in_row(grid, row, digit):
    for i in range(9):
        if grid[row][i] == digit:
            return True
    return False

# Helper function to check if digit exists in col
def used_in_col(grid, col, digit):
    for i in range(9):
        if grid[i][col] == digit:
            return True
    return False

# Helper function to check if digit used in box
def used_in_box (grid, row, col, digit):
    for i in range(3):
        for j in range(3):
            if grid[i+row][j+col] == digit:
                return True
    return False

# Helper Function to decide if it is legal to use the digit
def location_safe(grid, row, col, digit):
    return (not used_in_row(grid, row, digit) and 
            not used_in_col(grid, col, digit) and 
            not used_in_box(grid, row-row%3, col-col%3, digit))


def solver(grid):
    # A list of the empty locations in the grid
    empty_list = [0,0]

    # if there is no more empty location we are done
    if (not find_empty_location(grid, empty_list)):
        return True

    row = empty_list[0]
    col = empty_list[1]

    # let's try digits from 1 to 9
    for digit in range(1,10):

        if location_safe(grid, row, col, digit):
            # Make a temp assign
            grid[row][col] = digit

            # If solution is accepted 
            if solver(grid):
                return True

            # If the solution is not accepted
            grid[row][col] = 0

    # Trigger Backtracking
    return False

# Helper function to make sure the input is correct
def valid_input(line):
    
    # If more than 9 numbers entered show an error
    if len(line) != 9:
        print("Each line should be 9 numbers")
        return False
    
    for num in line:
        if not num.isdigit() or int(num) > 9:
            return False
    
    return True

if __name__ == "__main__":
    # Define 2D grid
    grid = list()

    print("Please enter the 9x9 Soduku board, use 0 for empty square")
    print("Seperate by space, enter a line then hit enter:")

    # Read the Sudoko input
    i = 0
    while i < 9:
        line = sys.stdin.readline().split()
        if valid_input(line):
            intline = [int(num) for num in line]
            grid.append(intline)
            i = i + 1
        else:
            print("input should be numbers between 0-9")

    if solver(grid):
        print_grid(grid)
    else:
        print("No Solution could be found!")