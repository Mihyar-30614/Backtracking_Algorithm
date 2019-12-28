import sys

# Helper function to print the output
def print_solution(solution):
    print("")
    for i in range(size):
        line = ''
        for j in range(size):
            line += str(solution[i][j]) + " "
        print(line)

# Helper function to make sure coordinates good
def isSafe(maze, x, y):
    if x>=0 and x<size and y>=0 and y<size and maze[x][y] == 1:
        return True
    return False

# Solver function
def solver(maze, x, y, solution):
    
    # Base case
    if x == size-1 and y == size-1:
        solution[x][y] = 1
        return True

    if isSafe(maze, x, y):
        solution[x][y] = 1

        # Move along X-axis
        if solver(maze, x+1, y, solution):
            return True

        # if not possible move to y direction
        if solver(maze, x, y+1, solution):
            return True
        
        # if none of the movements leads to solution
        solution[x][y] = 0
        return False

# Main function
if __name__ == "__main__":

    maze = list()

    # get input the size of the maze
    print("Please enter the size of the maze: ")
    temp = sys.stdin.readline().split()
    size = int(temp[0])

    # Get the structure of the maze
    print("Enter the maze struct sperated by space where 0 is a block: ")
    for i in range(size):
        line = sys.stdin.readline().split()
        intline = [int(num) for num in line]
        maze.append(intline)

    solution = [[0 for i in range(size)] for j in range(size)]

    if solver(maze, 0, 0, solution):
        print_solution(solution)
    else:
        print("No Solution Could be Found!")