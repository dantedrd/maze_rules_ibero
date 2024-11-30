from experta import KnowledgeEngine, Fact, Rule, TEST

from Maze import Maze
from rule_solver import RuleSolver
from Maze_GUI import MazeGUI

def main():
    maze_data = [
        [0, 1, 0, 0],
        [0, 1, 0, 1],
        [0, 0, 0, 1],
        [1, 1, 0, 0],
    ]

    maze = Maze(maze_data)
    solver = RuleSolver(maze)
    gui = MazeGUI(maze)
    print("goal  main")
    print(maze.goal)
    solver.reset()
    solver.declare(Fact(position=maze.start))  # Posición inicial
    solver.declare(Fact(goal=maze.goal))
    gui.start_solver(solver)
    gui.start()


if __name__ == "__main__":
    main()