import random
import mcschematic

# Maze dimensions
maze_width, maze_height = 10, 10

# Directions for movement (right, down, left, up)
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def initialize_maze(width, height):
    return [[1 for _ in range(width)] for _ in range(height)]

def print_maze(maze):
    for row in maze:
        print("".join(['#' if cell == 1 else ' ' for cell in row]))

def is_valid_move(maze, x, y):
    if x < 0 or x >= maze_width or y < 0 or y >= maze_height:
        return False
    if maze[y][x] == 0:
        return False
    return True

def generate_maze(maze, x, y):
    maze[y][x] = 0
    random.shuffle(directions)
    for dx, dy in directions:
        nx, ny = x + dx * 2, y + dy * 2
        if is_valid_move(maze, nx, ny):
            maze[y + dy][x + dx] = 0
            generate_maze(maze, nx, ny)

def put_in_world(width, height, outputPath):
    schem = mcschematic.MCSchematic()
    maze = initialize_maze(width, height)
    generate_maze(maze, 0, 0)

    for y, row in enumerate(maze):
        for x, col in enumerate(row):
            if col:
                schem.setBlock((x, 0, y), "minecraft:oak_leaves")
                schem.setBlock((x, 1, y), "minecraft:oak_leaves")
            else:
                schem.setBlock((x, -1, y), "minecraft:grass")
    
    schem.save("mazes", outputPath, mcschematic.Version.JE_1_18_2)
