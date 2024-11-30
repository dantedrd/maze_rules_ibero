class Maze:
    def __init__(self, grid):
        self.grid = grid
        self.start = (0, 0)  # Posición inicial
        self.goal = (len(grid) - 1, len(grid[0]) - 1)  # Meta
    
    def is_valid_move(self, position):
        x, y = position
        return 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]) and self.grid[x][y] == 0

    def move(self, position, direction):
        x, y = position
        if direction == "right":
            return (x, y + 1)
        elif direction == "left":
            return (x, y - 1)
        elif direction == "up":
            return (x - 1, y)
        elif direction == "down":
            return (x + 1, y)
        return position