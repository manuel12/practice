import csv
import math
from collections import Counter
from random import random


dataset_filename = 'colors.csv'

def load_colors(filename):
	with open(filename) as dataset_filename:
		lines = csv.reader(dataset_filename)
		for line in lines:
			yield tuple(float(y) for y in line[0:3]), line[3]

def generate_colors(count=100):
	for i in range(count):
		yield (random(), random(), random())

def color_distance(color1, color2):
	# channels = zip(color1, color2)
	# sum_distance_squared = 0
	# for c1, c2 in channels:
	# 	sum_distance_squared += (c1 - c2) ** 2
	# return math.sqrt(sum_distance_squared)
	return math.sqrt(sum((x[0] - x[1]) ** 2 for x in zip(
		color1, color2)))

def nearest_neighbors(model_colors, num_neighbors):
	model = list(model_colors)
	target = yield
	while True:
		distances = sorted(
			((color_distance(c[0], target), c) for c in model),
		)	
		target = yield [
			d[1] for d in distances[0:num_neighbors]
		]

model_colors = load_colors(dataset_filename)
target_colors = generate_colors(3)
get_neighbors = nearest_neighbors(model_colors, 5)
next(get_neighbors)

for color in target_colors:
	distances = get_neighbors.send(color)
	print(color)
	for d in distances:
		print(color_distance(color, d[0]), d[1])


def write_results(filename="output.csv"):
	with open(filename, "w") as file:
		writer = csv.writer(file)
		while True:
			color, name = yield
			writer.writerow(list(color) + [name])


results = write_results()
next(results)
for i in range(3):
	print(i)
	results.send(((i, i, i), i * 10))



# Page: 20

def name_colors(get_neighbors):
	color = yield
	while True:
		near = get_neighbors.send(color)
		name_guess = Counter(n[1] for n in near
			).most_common(1)[0][0]
		color = yield name_guess

def process_colors(dataset_filename="colors.csv"):
	model_colors = load_colors(dataset_filename)
	get_neighbors = nearest_neighbors(model_colors, 5)
	get_color_name = name_colors(get_neighbors)
	output = write_results()
	next(output)
	next(get_neighbors)
	next(get_color_name)

	for color in generate_colors():
		name = get_color_name.send(color)
		output.send((color, name))

process_colors()
