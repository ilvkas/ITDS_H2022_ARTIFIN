from pacman_module.game import Agent, Directions
from pacman_module.util import Queue


def key(state):
    """Returns a key identifier that uniquely identifies a given Pacman game state composed of: the agent's position
    and the current game state.

    Arguments:
        state: a pacman game state. For mor info, refer to pacman_module: `pacman.py` (GameState)

    Returns:
        A hashable key tuple composed of current Pacman Position and current Food State
    """

    return (
        # add pacman's position (have a look at GameState to find the proper function)
        # add food state (have a look at GameState to find the proper 'grid boolean food' state function)
        state.getPacmanPosition(), state.getFood()
    )


class PacmanAgent(Agent):
    """ Implements a Pacman agent based on breadth-first search (BFS)."""

    def __init__(self):
        super().__init__()

        self.moves = None

    def get_action(self, state):
        """Given a Pacman game state, returns a list of legal moves to solve
        the search layout based on breadth-first-search (BFS)

        Arguments:
            state: a pacman game state. For mor info, refer to pacman_module: `pacman.py` (e.g. GameState)

        Returns:
            A legal pacman move. For mor info, refer to pacman_module: `game.py` (Directions)
        """

        if self.moves is None:
            self.moves = self.bfs(state) # explores possible moves by using BFS

        if self.moves:
            return self.moves.pop(0) # retrieves first move provided there are some
        else:
            return Directions.STOP

    def bfs(self, state):
        """Given a Pacman game state, returns a list of legal moves to solve
        the Pacman search problem using Breadth First Search.

        Arguments:
            state: a pacman game state. For mor info, refer to pacman_module: `pacman.py` or 'game.py'.

        Returns:
            A path (list) of legal moves.
        """

        path = []
        frontier = Queue() # initialise the corresponding data structure 
        frontier.push((state, path)) # add current state and path to the fringe
        explored = set()  # define a data structure to keep track of explored positions

        while True:
            # check whether the fringe is empty so as to return an empty path
            if frontier.isEmpty():
                return []

            # get current solution from fringe, composed of current state and path
            current, path = frontier.pop()

            # get current state and check whether there's no more food to eat
            if current.getFood().count() == 0:
                return path # return solution

            # get current agent position
            current_key = key(current)

            # if current agent position is explored, don't do anything
            if current_key in explored:
                continue
            else:
            # add  current position to the explored positions
                explored.add(current_key)

            for successor, action in current.generatePacmanSuccessors():
                frontier.push((successor, path + [action]))

        return path # return valid moves
