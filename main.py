import numpy as np
from createAnimation import createAnimation

# declare maze visualization constants, maze
b = np.array([255, 255, 255]) 	# blank, white
w = np.array([0, 0, 0]) 		# wall, black
t = np.array([255, 255, 0]) 	# treasure, yellow
e = np.array([255, 0, 0])		# enemy, red
p = np.array([0, 255, 0])		# player, green

starting_pos = (0, 0)
maze = np.array([[b, b, b, b, b, b, b, b, b, t],
				 [w, w, w, b, w, w, w, w, w, w],
				 [t, w, b, b, b, b, b, b, b, w],
				 [b, w, b, w, w, w, w, w, b, w],
				 [b, b, b, w, t, b, b, b, b, w],
				 [w, w, w, w, w, w, w, w, b, w],
				 [e, b, b, b, b, b, b, b, b, b],
				 [t, e, b, b, w, w, w, w, w, w],
				 [t, e, b, b, b, b, b, b, b, b],
				 [e, b, b, b, w, w, w, w, w, t]])

moves = ['r'] * 9 + ['l'] * 6 + ['d'] * 2 + ['l'] + ['d'] * 2 + ['l'] * 2 + ['u'] * 2 + ['d']

createAnimation(maze, starting_pos, moves)