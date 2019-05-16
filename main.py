import numpy as np
from qlearning import qlearn, solve
from createAnimation import createAnimation
import matplotlib
import matplotlib.pyplot as plt

# maze visualization constants
b = 'b'
w = 'w'
t = 't'
e = 'e'

# starting_pos = (15, 9)
# maze = np.array([[b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
# 				 [t, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, t],
# 				 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
# 				 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b],
# 				 [b, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, b],
# 				 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
# 				 [w, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, w],
# 				 [w, w, w, w, b, w, b, b, b, b, b, b, b, w, b, w, w, w, w],
# 				 [w, w, w, w, b, w, b, w, w, b, w, w, b, w, b, w, w, w, w],
# 				 [w, w, w, w, b, b, b, w, b, b, b, w, b, b, b, w, w, w, w],
# 				 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
# 				 [w, w, w, w, b, w, b, b, b, t, b, b, b, w, b, w, w, w, w],
# 				 [w, w, w, w, b, w, b, w, w, w, w, w, b, w, b, w, w, w, w],
# 				 [b, b, b, b, b, b, b, b, b, w, b, b, b, b, b, b, b, b, b],
# 				 [b, w, w, w, b, w, w, w, b, w, b, w, w, w, b, w, w, w, b],
# 				 [t, b, b, w, b, b, b, b, b, b, b, b, b, b, b, w, b, b, t],
# 				 [w, w, b, w, b, w, b, w, w, w, w, w, b, w, b, w, b, w, w],
# 				 [b, b, b, b, b, w, b, b, b, w, b, b, b, w, b, b, b, b, b],
# 				 [b, w, w, w, w, w, w, w, b, w, b, w, w, w, w, w, w, w, b],
# 				 [b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b, b]])

starting_pos = (2, 2)
maze = np.array([[t, b, b, w, t],
				 [w, w, b, w, b],
				 [b, w, b, w, b],
				 [b, b, b, w, b],
				 [t, w, b, b, b]])

# starting_pos = (0, 0)
# maze = np.array([[b, b, t],
# 				 [b, b, b],
#  				 [t, b, b]])

print('Constructing Q table...', end=' ', flush=True)
q_table, n_time_steps = qlearn(maze, starting_pos)
print('done')

print('Solving...', end=' ', flush=True)
moves = solve(maze, starting_pos, q_table)
print('done')

print('Calculated path:', moves)

print('Animating / Creating GIF...', end=' ', flush=True)
createAnimation(maze, starting_pos, moves)
print('done')

plt.plot(n_time_steps)
plt.xlabel('Episode')
plt.ylabel('Number of time steps')
plt.show()