import tkinter as tk
import sys
from experta import KnowledgeEngine, Fact,MATCH, Rule, TEST

class MazeGUI:
    def __init__(self, maze):
        self.maze = maze
        self.cell_size = 50  # Tamaño de cada celda
        self.initPosition= maze.start
        self.initGoalPosition= maze.goal
        self.current_position = maze.start
        self.goal_position = maze.goal

        # Crear ventana y lienzo
        self.root = tk.Tk()
        self.root.title("Maze Solver")
        self.canvas = tk.Canvas(
            self.root,
            width=len(maze.grid[0]) * self.cell_size,
            height=len(maze.grid) * self.cell_size,
        )
        self.canvas.pack()

        # Dibujar el laberinto
        self.draw_maze()

    def draw_maze(self):
        for i, row in enumerate(self.maze.grid):
            for j, cell in enumerate(row):
                color = "white" if cell == 0 else "black"
                self.canvas.create_rectangle(
                    j * self.cell_size,
                    i * self.cell_size,
                    (j + 1) * self.cell_size,
                    (i + 1) * self.cell_size,
                    fill=color,
                )
        self.update_position(self.current_position, "blue")
        self.update_position(self.goal_position, "green")

    def update_position(self, position, color="blue",init=0):
        # Limpiar la posición anterior
        self.canvas.create_rectangle(
            self.current_position[1] * self.cell_size,
            self.current_position[0] * self.cell_size,
            (self.current_position[1] + 1) * self.cell_size,
            (self.current_position[0] + 1) * self.cell_size,
            fill="white",
        )
        # Dibujar la posición actual
        self.canvas.create_rectangle(
            position[1] * self.cell_size,
            position[0] * self.cell_size,
            (position[1] + 1) * self.cell_size,
            (position[0] + 1) * self.cell_size,
            fill=color,
        )
        if init==0:
           self.current_position = self.initPosition
        else:
           self.current_position = position

    def start_solver(self, solver):
        def step():
            if self.current_position == self.goal_position:
                print("Goal reached!")
                return

            solver.run()
            for fact in solver.facts.values():
                if fact.get("move"):
                    move = fact["move"]
                    print(f"Movimiento: {move}")

                    # Actualizar la posición actual
                    x, y = self.current_position
                    #print(f"{x} {y}")
                    if move == "down":
                        positionUpdate = (x + 1, y)
                    elif move == "up":
                        positionUpdate = (x - 1, y)
                    elif move == "right":
                        positionUpdate = (x, y + 1)
                    elif move == "left":
                        positionUpdate = (x, y - 1)

                    
                    #if x<=1:
                    #print(y)
                    if self.maze.is_valid_move(positionUpdate):
                        self.current_position=positionUpdate
                        self.update_position(positionUpdate, "blue",1)
                        solver.reset()
                        solver.declare(Fact(position=positionUpdate))
                        solver.declare(Fact(goal=self.goal_position))
                    else:
                       print(f"Movimiento inválido hacia {move} (pared o fuera de límites).")
                    break
                    # Actualizar la posición en la GUI
                    
                    break

            self.root.after(500, step)

        step()

    def start(self):
        self.root.mainloop()