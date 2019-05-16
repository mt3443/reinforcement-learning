import numpy as np
import itertools
from state import State
from copy import deepcopy

b = 'b'
e = 'e'
t = 't'
w = 'w'

u = 'u'
d = 'd'
l = 'l'
r = 'r'

alpha = 0.1
gamma = 0.6
epsilon = 0.1

n_episodes = 1000

actions = [u, d, l, r]

np.random.seed(0)

all_states = []

maze = None

def next_reward_done(current_state, move):

	global maze

	x, y = current_state.pos
	treasures = deepcopy(current_state.treasures)

	if len(treasures) == 0:
		return None

	if move == u and x != 0 and maze[x - 1][y] != w:
		new_pos = x - 1, y
	elif move == d and x != len(maze) - 1 and maze[x + 1][y] != w:
		new_pos = x + 1, y
	elif move == l and y != 0 and maze[x][y - 1] != w:
		new_pos = x, y - 1
	elif move == r and y != len(maze[0]) - 1 and maze[x][y + 1] != w:
		new_pos = x, y + 1
	else:
		new_pos = x, y

	if maze[new_pos] == t:
		reward = 100
	elif maze[new_pos] == e:
		reward = -10
	else:
		reward = -1

	next_state = State(new_pos, treasures)

	if len(next_state.treasures) == 0:
		done = True
	else:
		done = False

	return all_states.index(next_state), reward, done

def qlearn(maze_, starting_pos):
	global maze
	maze = maze_

	treasures = np.argwhere(maze == t).tolist()

	# get all states
	global all_states
	for i in range(len(maze)):
		for j in range(len(maze[0])):
			if np.array_equal(maze[i][j], w):
				continue

			for k in range(len(treasures)):
				combinations = list(itertools.combinations(treasures, k + 1))

				for x in range(len(combinations)):
					all_states.append(State((i, j), list(combinations[x])))

	# construct reward table
	reward_table = []
	for i in range(len(all_states)):
		reward_table.append({u: next_reward_done(all_states[i], u),
							d: next_reward_done(all_states[i], d),
							l: next_reward_done(all_states[i], l),
							r: next_reward_done(all_states[i], r)})

	# initialize q table
	q_table = np.zeros((len(all_states), 4))

	for i in range(n_episodes):
		
		state = State(starting_pos, treasures)

		done = False

		while not done:

			state_index = all_states.index(state)

			if np.random.uniform() < epsilon:
				# explore
				action = np.random.choice(actions)
				action_index = actions.index(action)
			else:
				# exploit
				action_index = np.argmax(q_table[state_index])
				action = actions[action_index]

			next_state_index, reward, done = next_reward_done(state, action)

			old_q = q_table[state_index, action_index]
			next_max = np.max(q_table[next_state_index])

			new_q = (1 - alpha) * old_q + alpha * (reward + gamma * next_max)
			q_table[state_index, action_index] = new_q

			state = all_states[next_state_index]
	
	return q_table

def solve(maze, starting_pos, q_table):
	
	global all_states

	treasures = np.argwhere(maze == t).tolist()
	state = State(starting_pos, treasures)
	done = False

	moves = []

	while not done:
		state_index = all_states.index(state)
		move = actions[np.argmax(q_table[state_index])]
		moves.append(move)
		next_state_index, reward, done = next_reward_done(state, move)
		next_state = all_states[next_state_index]
		state = next_state

	return moves