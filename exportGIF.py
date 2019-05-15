import numpy as np
from array2gif import write_gif

def to_gif(arrays, file_name):
	'''Exports a list of given arrays as an animated gif with the given file name'''

	for i in range(len(arrays)):
		arrays[i] = np.transpose(arrays[i], (1, 0, 2))

	max_pixels = 500

	width = arrays[0].shape[0]
	height = arrays[0].shape[1]
	scaling_factor = min(int(max_pixels / width), int(max_pixels / height))
	fps = 3
	new_width = width * scaling_factor
	new_height = height * scaling_factor

	new_arrays = []

	for i in range(len(arrays)):
		temp = np.zeros((new_width, new_height, 3))
		for j in range(new_width):
			for k in range(new_height):
				temp[j][k] = arrays[i][int(j / scaling_factor)][int(k / scaling_factor)]
		new_arrays.append(temp)

	write_gif(new_arrays, file_name, fps)