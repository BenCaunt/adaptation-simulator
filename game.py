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

yeetus = species("ya boi chips ahoy",3,6,2,10,5,4,4,0,4,6,5,6,5,4,4,2)
carmen = species("carmen ;)",5,6,0,0,2,1,3,0,1,2,3,6,2,6,5,1)

#multiplier applied to each species population when a hurricane event occurs
hurricane_multi = 0.97

#multiplier applied to each species population when a mass extinction event occurs
extinction_multi = 0.01


#one easy function that reproduces every species while just taking up one line inside the for-loop
def reproduce_all():
	reproduce(yeetus)
	reproduce(carmen)

def main():
	for generation in range(1,10):
		reproduce_all()
		event = bad_boi()
		print(event)
		if event == 1:
			yeetus.population = yeetus.population * hurricane_multi
			carmen.population = carmen.propulation * hurricane_multi
			print('a hurricane has occured!!!;  Each species population has been decreased by 3%')

		elif event == 2:
			yeetus.population = yeetus.population * extinction_multi
			carmen.population = yeetus.population * extinction_multi
			print('a mass-extinction event has occured; each species population has been decreased by 99.9%')

		population_total = sum([carmen.population, yeetus.population])
		num_conflict = (0.1)*population_total
		print(f"Ben's population is: {yeetus.population}")
		print(f"Carmen's population is: {carmen.population}")
		print(f"total population is: {population_total}")
		#calling the reproduce all function we created earlier

if __name__ == '__main__':
	main()
