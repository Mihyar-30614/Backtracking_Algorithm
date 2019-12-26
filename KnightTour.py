# Cheesboard size
size = 8

# Helper Function to print Solution
def printSolution(board):
    for i in range(size):
        for j in range(size):
            print(board[i][j], end=' ')
        print()

# Helper function to check if i,j are in n*n board
def isSafe(board, new_x, new_y):
    if (new_x >= 0 and new_y >= 0 and new_x < size and new_y < size and board[new_x][new_y] == -1):
        return True
    return False

# Solver function to solve the issue
def solver(board, current_x, current_y, move_x, move_y, counter):
    
    # If all visited, we're done
    if counter == size**2:
        return True

    # Try all the possible solutions for current position
    for i in range(8):
        new_x = current_x + move_x[i]
        new_y = current_y + move_y[i]

        if isSafe(board, new_x, new_y):
            board[new_x][new_y] = counter
            if solver(board, new_x, new_y, move_x, move_y, counter+1):
                return True
            else:
                # Backtracking solution
                board[new_x][new_y] = -1
    return False

# Driver Function
if __name__ == "__main__":

    # Initialize Board with -1, Knight start at first position
    board = [[-1 for i in range(size)] for i in range(size)]
    board[0][0] = 0

    # Possible moves for a Knight
    move_x = [2, 1, -1, -2, -2, -1, 1, 2] 
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Counter for the Knight's move
    counter = 1

    if not solver(board, 0, 0, move_x, move_y, counter):
        print("Solution could not be found.")
    else:
        printSolution(board)