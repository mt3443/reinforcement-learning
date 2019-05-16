import numpy as np
from qlearning import qlearn, solve
from createAnimation import createAnimation

# maze visualization constants
b = 'b'
w = 'w'
t = 't'
e = 'e'

starting_pos = (15, 9)
maze = np.array([[b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
				 [t, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
				 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
				 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
				 [b, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, b],
				 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
				 [w, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, w],
				 [w, w, w, w, b, w, b, b, b, b, b, b, b, w, b, w, w, w, w],
				 [w, w, w, w, b, w, b, w, w, b, w, w, b, w, b, w, w, w, w],
				 [w, w, w, w, b, b, b, w, b, b, b, w, b, b, b, w, w, w, w],
				 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
				 [w, w, w, w, b, w, b, b, b, b, b, b, b, w, b, w, w, w, w],
				 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
				 [b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
				 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
				 [b, b, b, w, b, b, b, b, b, b, b, b, b, b, b, w, b, b, b],
				 [w, w, b, w, b, w, b, w, w, w, w, w, b, w, b, w, b, w, w],
				 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
				 [b, w, w, w, w, w, w, w, b, w, b, w, w, w, w, w, w, w, b],
				 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]])

# starting_pos = (2, 2)
# maze = np.array([[b, b, b, w, b],
# 				 [w, w, b, w, b],
# 				 [b, b, b, b, b],
# 				 [b, b, b, b, b],
# 				 [t, w, b, w, b]])

# starting_pos = (0, 0)
# maze = np.array([[b, b],
# 				 [w, t]])

print('Constructing Q Table...', end=' ', flush=True)
q_table = qlearn(maze, starting_pos)
print('done')

print('Solving...', end=' ', flush=True)
moves = solve(maze, starting_pos, q_table)
print('done')

# print(moves)

# print('Creating GIF...', end=' ', flush=True)
# createAnimation(maze, starting_pos, moves)
# print('done')