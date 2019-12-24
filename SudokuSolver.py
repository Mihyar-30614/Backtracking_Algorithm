# Helper function to print Grid
def print_grid(grid):
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

if __name__ == "__main__":
    # Define 2D grid
    grid = [[3,0,6,5,0,8,4,0,0], 
            [5,2,0,0,0,0,0,0,0], 
            [0,8,7,0,0,0,0,3,1], 
            [0,0,3,0,1,0,0,8,0], 
            [9,0,0,8,6,3,0,0,5], 
            [0,5,0,0,9,0,6,0,0], 
            [1,3,0,0,0,0,2,5,0], 
            [0,0,0,0,0,0,0,7,4], 
            [0,0,5,2,0,6,3,0,0]]

    if solver(grid):
        print_grid(grid)
    else:
        print("No Solution could be found!")