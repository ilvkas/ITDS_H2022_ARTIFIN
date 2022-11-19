import argparse
import importlib

from pacman_module.pacman import runGame


if __name__ == '__main__':
    """
    This file is reponsible for running a pacman agent and solving the game. To use it, enter the following commands 
    on your console: 
    - python3 run.py --agent human --layout large # runs a Human-based Pacman Agent on a "large" layout
    - python3 run.py --agent dfs_ex --layout large # runs a DFS-based Pacman Agent on a "large" layout
    - python3 run.py --agent bfs_ex --layout large # runs a BFS-based Pacman Agent on a "large" layout
    
    additional examples are:
    - python3 run.py --agent human --layout medium # runs a Human-based Pacman Agent on a "medium" layout
    - python3 run.py --agent human --layout small # runs a Human-based Pacman Agent on a "small" layout
    
    The layout parameter defines the agent's environment. It can have the following values: small, medium, large
    You can create your own environment, by creating your own a '.lay' file and placing it under "pacman_module/layouts".
    Have a look at the existing .lay files to define your own test environment. '%' defines a wall, 'P' defines the initial
    agent location, '.' defines a food item. You need your environment to be closed by walls so as that the problem is
    constrained.
    
    Solutions shall be send by each group per email until Sunday, 16th of October with the e-mail Subject 'ARTIFIN: Pacman Agent'.
    Please comment your code if needed and be able to explain in. It is suggested that all group participants work
    together on the 2 assignments and not separately on their own.
    Under 'pacman_module.utils' you will find there a set of data structures that can be useful for solving the exercise.
    """
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '-a',
        '--agent',
        default='dfs',
        help='Python module containing a `PacmanAgent` class.',
    )

    parser.add_argument(
        '-l',
        '--layout',
        default='large',
        help='Maze layout (from layouts folder).',
    )

    parser.add_argument(
        '-ng',
        '--nographics',
        help='Disable the graphical display of the game.',
        default=False,
        action='store_true',
    )

    args = parser.parse_args()

    score, time, nodes = runGame(
        layout_name=args.layout,
        pacman=importlib.import_module(args.agent).PacmanAgent(),
        ghosts=[],
        beliefstateagent=None,
        displayGraphics=not args.nographics,
        expout=0.0,
        hiddenGhosts=False,
    )

    print(f"Final Score: {score}")
    print(f"Computational time: {time}")
    print(f"Expanded nodes: {nodes}")
