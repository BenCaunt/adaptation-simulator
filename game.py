#imports from our other file "creature.py"
from creature import reproduce
from creature import species
from creature import bad_boi

#other libraries that we may or may not need
import random
import numpy as np
import time
import os
import matplotlib.pyplot as plt

#herbivore = 1;  omnivore = 2;  carnivore = 3
#skeleton 1 = exo, 2 = endo, 3 = none

yeetus = species("ya boi chips ahoy",3,6,2,10,3,4,4,0,4,6,5,6,5,4,4,2)
carmen = species("carmen ;)" ,5,6,0,0,2,1,3,0,1,2,3,6,2,6,5,1)

#multiplier applied to each species population when a hurricane event occurs
hurricane_multi = 0.90
hurricane_prob = 3
#multiplier applied to each species population when a mass extinction event occurs
extinction_multi = 0.01
extinction_prob = 10000


#one easy function that reproduces every species while just taking up one line inside the for-loop
def reproduce_all():
	reproduce(yeetus)
	reproduce(carmen)

def main():
	for generation in range(1000):
		species_num = 2

		#calling the reproduce all function we created earlier
		reproduce_all()
		#randomly generatd value between (0, hurricane_prob)
		a = random.randint(0,hurricane_prob)
		#randomly generatd value between (1, extinction_prob)
		b = random.randint(1,extinction_prob)
		event = bad_boi(a ,b)
		print(event)
		#if the event variable is assigned a 1 then a hurricane occurs
		if event == 1:
			#generates random number for hurricane thingy
			x = []
			for i in range(0,species_num):
				x.append(random.uniform(1,0.5)) #¸  <<<<<wut is this character
			#the population is multiplied by the percentage that was defined in the hurricane_multi variable
			yeetus.population = round(yeetus.population * x[0])
			carmen.population = round(carmen.population * x[1])
			print('a hurricane has occured!!!;  Each species population has been decreased by an average of {0}%'.format(sum(x)/len(x)))

		elif event == 2:
			yeetus.population = round(yeetus.population * extinction_multi)
			carmen.population = round(yeetus.population * extinction_multi)
			print('a mass-extinction event has occured; each species population has been decreased by 0.1%')

		population_total = sum([carmen.population, yeetus.population])
		num_conflict = (0.1)*population_total
		print(f"Ben's population is: {yeetus.population}")
		print(f"Carmen's population is: {carmen.population}")
		print(f"total population is: {population_total}")

if __name__ == '__main__':
	main()
