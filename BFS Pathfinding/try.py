from collections import deque

def bfs_maze_solver(maze):
    def is_valid(x, y): #checks if the given cell is a part of the maze or not
        return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] != '#'
    

    def get_neighbors(x, y):
        neighbors = []
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                neighbors.append((nx, ny))
        return neighbors

    start = None
    end = None

    for x in range(len(maze)):
        for y in range(len(maze[0])):
            if maze[x][y] == 'S':
                start = (x, y)
            elif maze[x][y] == 'E':
                end = (x, y)

 
    queue = deque([(start, [])])
    visited = set()

    while queue:
        (x, y), path = queue.popleft()

        if (x, y) == end:
            return path
        

        if (x, y) not in visited:
            visited.add((x, y))
        

            for nx, ny in get_neighbors(x, y):
                queue.append(((nx, ny), path + [(nx, ny)]))

    return "No path found in the maze."

# Example usage:
maze = [
    ['#', 'S', '#', '#', '.', '#'],
    ['.', '.', '.', '.', '.', '#'],
    ['#', '.', '#', '#', '.', '#'],
    ['#', '.', '.', '.', '.', '.'],
    ['#', '#', '#', '#', 'E', '#'],
]

solution = bfs_maze_solver(maze)
# maze[1]=='+'

if solution:
    print("Path found:", solution)
    

    
    # for row in maze:
    #     print(" ".join(row))
    # for i in range(len(maze)):
    #     for j in range(len(maze[0])):
    #         maze[i][j] 


else:
    print("No path found in the maze.")

    