from time import time
from puzzle import Puzzle
from DFS import dfs
from BFS import bfs
from manhatten import bfs_manhattan

import numpy as np

initial_state= [2, 8, 3,
                1, 6, 4,
                7, 0, 5]

goal_state= [2, 0, 8,
            1, 6, 3,
            7, 5, 4]

Puzzle.num_of_instances=0
t0=time()
dfs_solution=dfs(initial_state)
t1=time()-t0
print('Solution:', dfs_solution)
print('space:',Puzzle.num_of_instances)
print('time:',t1,"seconds")
print()

Puzzle.num_of_instances=0
t2=time()
bfs_solution=bfs(initial_state)
t3=time()-t2
print('Solution:', bfs_solution)
print('space:',Puzzle.num_of_instances)
print('time:',t3,"seconds")
print()


Puzzle.num_of_instances=0
t4=time()
manhatten_solution=bfs_manhattan(initial_state)
t5=time()-t4
print('Solution:', manhatten_solution)
print('space:',Puzzle.num_of_instances)
print('time:',t5,"seconds")
print()