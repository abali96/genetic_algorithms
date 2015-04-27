from __future__ import division
import itertools
import random
import numpy

# maximize function on range 0 to 100

def f(x):
	return x*x

def gen_strings(str_len, num_str):
	strs = list()
	for i in range(num_str):
		strs.append('')

	for i in range(num_str):
		for j in range(str_len):
			strs[i] += str(int(bool(random.getrandbits(1))))

	return strs
	

def compute_fitness(binary_list):
	fitness_list = list()

	function_output = map(f,map(lambda x: int(x, 2), binary_list))
	avg = reduce(lambda x, y: x + y, function_output)/len(function_output) # we cant assume avg isn't 0

	for i in range(len(binary_list)):
		fitness_list.append(function_output[i]/avg)
	
	return map(lambda x: x/len(binary_list), fitness_list) # sum of these elements should be 1
	

def roulette(strs):
	spins = list()
	if compute_fitness:
		ranges = numpy.cumsum(compute_fitness(strs))[:-1]

		for i in range(len(strs)):
			spin_val = random.random()
			index = 0

			while index < len(strs) - 1 and spin_val > ranges[index]:
				index += 1

			spins.append(strs[index])

	return spins


def mutate(population):
	if random.randrange(0, 200) is 0:
		index1 = random.randrange(0, len(population))
		index2 = random.randrange(0, len(population[0]))
		population = map(lambda x: list(x), population)
		if population[index1][index2] is "1":
			population[index1][index2] = "0"
		else:
			population[index1][index2] = "1"

	return map(lambda x: "".join(x), population)
	

def crossover(new_population):
	new_population = map(lambda x: list(x), new_population)
	for i in range(len(new_population)//2):
		cross_index = random.randrange(1, len(new_population))
		# print "crossing over " + str(new_population[i]) + " with " + str(new_population[-i-1]) + "at index " + str(cross_index)

		for j in range(cross_index, len(new_population[0])):
			temp = new_population[i][j]
			new_population[i][j] = new_population[-i-1][j]
			new_population[-i-1][j] = temp

	return map(lambda x: "".join(x), new_population)

def maximize():
	population = gen_strings(5, 200)
	while population[1:] != population[:-1]: # could use a better condition
		population = roulette(population)
		population = crossover(population)
		population = mutate(population)

	print population

maximize()