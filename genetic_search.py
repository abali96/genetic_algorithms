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
	
	if avg is 0:
		return False

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
	if random.randrange(0, len(population * len(population[0]))) is 0:
		index1 = random.randrange(0, len(population))
		index2 = random.randrange(0, len(population[0]))
		population = map(lambda x: list(x), population)
		population[index1][index2] = str(int(not (bool(int(population[index1[index2]]))))) # have to convert this to a list first!
	return map(lambda x: "".join(x), population)
	

def crossover(new_population):
	print new_population
	new_population = map(lambda x: list(x), new_population)
	for i in range(len(new_population)//2):
		cross_index = random.randrange(1, len(new_population))
		print "crossing over " + str(new_population[i]) + "with " + str(new_population[-i-1]) + "at index " + str(cross_index)
		# print i
		# print new_population[i]

		# for j in range(cross_index, len(new_population[0])):
		# 	temp = new_population[i][j]
		# 	new_population[i][j] = new_population[-i][j]
		# 	new_population[-i][j] = temp

	print new_population
	return map(lambda x: "".join(x), new_population)

def maximize():
	population = gen_strings(5, 4)
	for i in range(1):
		population = roulette(population)
		if population and population[1:] is not population[-1:]:
			population = crossover(population)
			# population = mutate(population)
		else:
			population = gen_strings(5, 4)

	# check if the intervals in the fitness thing are even

maximize()