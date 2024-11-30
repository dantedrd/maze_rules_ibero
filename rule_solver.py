from experta import KnowledgeEngine, Fact,MATCH, Rule, TEST

class RuleSolver(KnowledgeEngine):
    def __init__(self, maze):
        super().__init__()
        self.maze = maze  # Guardar una referencia al laberinto
        self.visited_positions = set()
     
    @Rule(Fact(position=MATCH.position), Fact(goal=MATCH.goal),TEST(lambda position, goal: position[0] < goal[0]))
    def move_down(self,position,goal):
        print("move_down")
        print(position)
        print(goal)
        new_position = (position[0] + 1, position[1])
        if self.maze.is_valid_move(new_position):  # Verifica si el movimiento es válido
           print(f"Movimiento hacia abajo válido: {new_position}")
           self.declare(Fact(move="down"))
        else:
           print(f"Movimiento hacia abajo inválido o ya visitado: {new_position}")

    @Rule(Fact(position=MATCH.position), Fact(goal=MATCH.goal),TEST(lambda position, goal: position[0] > goal[0]))
    def move_up(self,position,goal):
        print("move_up")
        print(position)
        print(goal)
        new_position = (position[0] - 1, position[1])
        if self.maze.is_valid_move(new_position):  # Verifica si el movimiento es válido
           print(f"Movimiento hacia abajo válido: {new_position}")
           self.declare(Fact(move="down"))
        else:
           print(f"Movimiento hacia abajo inválido o ya visitado: {new_position}")
        #self.declare(Fact(move="up"))

    @Rule(Fact(position=MATCH.position), Fact(goal=MATCH.goal),TEST(lambda position, goal: position[1] < goal[1]))
    def move_right(self,position,goal):
        print("move_right")
        print(position)
        print(goal)
        new_position = (position[0], position[1]+1)
        if self.maze.is_valid_move(new_position):  # Verifica si el movimiento es válido
           print(f"Movimiento hacia abajo válido: {new_position}")
           self.declare(Fact(move="right"))
        else:
           print(f"Movimiento hacia abajo inválido o ya visitado: {new_position}")
        #self.declare(Fact(move="right"))

    @Rule(Fact(position=MATCH.position), Fact(goal=MATCH.goal),TEST(lambda position, goal: position[1] > goal[1]))
    def move_left(self,position,goal):
        print("move_left")
        print(position)
        print(goal)
        print("Rule triggered: Move left")
        new_position = (position[0], position[1]- 1)
        if self.maze.is_valid_move(new_position):  # Verifica si el movimiento es válido
           print(f"Movimiento hacia abajo válido: {new_position}")
           self.declare(Fact(move="down"))
        else:
           print(f"Movimiento hacia abajo inválido o ya visitado: {new_position}")
        #self.declare(Fact(move="left"))






