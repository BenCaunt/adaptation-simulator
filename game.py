#imports from our other file "creature.py"
from creature import reproduce
from creature import species
from creature import bad_boi
from creature import compete
from creature import mutate
#other libraries that we may or may not need
import random
import numpy as np
import time
import os
import matplotlib.pyplot as plt
plt.style.use('ggplot')

#herbivore = 1;  omnivore = 2;  carnivore = 3
#skeleton 1 = exo, 2 = endo, 3 = none

yeetus = species("ya boi chips ahoy",3,6,2,10,3,4,4,0,4,6,5,6,5,4,4,2)
carmen = species("carmen ;)" ,5,6,0,0,2,1,3,0,1,2,3,6,2,6,5,1)
david = species("tan line", 1, 1, 0, 3, 3, 1, 4, 10, 1, 4, 6, 2, 3, 2, 3, None)
jacey = species("'Daemon Volantes'", 3, 6, 0, 2, 1, 3, 3, 0, 2, 2, 3, 5, 3, 3, 3, 5)
ethan = species("Neotyrannus Satanus", 4, 2, 0, 2, 2, 6, 1, 2, 3, 4, 1 , 2, 6, 3, 3,4)
sarah = species("sarah", 3, 6, 0, 4, 3, 2, 1, 0, 2, 3, 2, 6, 3, 4, 5, 4)
kaleigh = species("kaleigh", 3, 6, 0, 6, 2, 3, 4, 4, 1, 2, 1, 2, 2, 4, 6, 3)
libby = species("libby", 3, 3, 0, 0, 6, 3, 4, 2, 2, 1, 5, 1, 2, 1, 4, 1)
aiden = species("aiden", 5, 3, 12, 12, 4, 3, 2, 8, 2, 4, 6, 3, 4, 4, 4, 2)
shep = species("Shep",4,5,0,6,2,6,4,10,3,2,5,3,2,4,5,6)

#all species in a population
biosphere = [yeetus,carmen,david,jacey,ethan,sarah,kaleigh, libby, aiden,shep]

#total in biosphere
species_num = 10

#multiplier applied to each species population when a hurricane event occurs
hurricane_multi = 0.90
hurricane_prob = 3
#multiplier applied to each species population when a mass extinction event occurs
extinction_multi = 0.01
extinction_prob = 10000

def main():
	for generation in range(3):
		#one easy function that reproduces every species while just taking up one line inside the for-loop
		def reproduce_all():
			for i in range(species_num):
				reproduce(biosphere[i])
		print(f"population in biosphere is {species_num} organisms")

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
				x.append(random.uniform(1,0.5)) #  <<<<<wut is this character
			#the population is multiplied by the percentage that was defined in the hurricane_multi variable
			yeetus.population = round(yeetus.population * x[0])
			carmen.population = round(carmen.population * x[1])
			david.population = round(david.population * x[2])
			jacey.population = round(jacey.population * x[3])
			ethan.population = round(ethan.population * x[4])
			sarah.population = round(sarah.population * x[5])
			kaleigh.population = round(kaleigh.population * x[6])
			libby.population = round(libby.population * x[7])
			aiden.population = round(aiden.population * x[8])
			shep.propulation = round(shep.population * x[9])
			print('a hurricane has occured!!!;  Each species population has been decreased by an average of ~{0}%'.format(round(100-(100*((sum(x)/len(x)))))))

		elif event == 2:
			yeetus.population = round(yeetus.population * extinction_multi)
			carmen.population = round(carmen.population * extinction_multi)
			david.population = round(david.population * extinction_multi)
			jacey.population = round(jacey.population * extinction_multi)
			ethan.population = round(ethan.population * extinction_multi)
			sarah.population = round(sarah.population * extinction_multis)
			kaleigh.population = round(kaleigh.population * extinction_multi)
			libby.population = round(libby.population * extinction_multi)
			aiden.population = round(aiden.population * extinction_multi)
			shep.population = round(shep.population * extinction_multi)
			print('a mass-extinction event has occured; each species population has been decreased by 0.1%')
		else:
			pass

		#loop for each time a conflict occurs
		for i in range(1000):
			#species conflict, see creature.py for more information
			compete(biosphere)
		for i in range(100):
			mutate(biosphere)

		population_total = sum([carmen.population, yeetus.population])
		num_conflict = (0.1)*population_total

		for i in range(species_num):
			print(f"{biosphere[i].name} has the population of {biosphere[i].population}")

		x = [yeetus.name,carmen.name,david.name,jacey.name,ethan.name,sarah.name,kaleigh.name, libby.name, aiden.name, shep.name]
		y = [yeetus.population,carmen.population,david.population,jacey.population,ethan.population,sarah.population,kaleigh.population, libby.population, aiden.population, shep.population]

		plt.bar(x, y, color='teal')
		plt.rcParams.update({'font.size': 20})
		plt.xlabel("Species'")
		plt.ylabel("population")
		plt.rcParams.update({'font.size': 22})
		plt.title(f"generation {i}")

		plt.xticks(x, x)

		plt.savefig(f"gen_{i}.png")


if __name__ == '__main__':
	main()

	x = [yeetus.name,carmen.name,david.name,jacey.name,ethan.name,sarah.name,kaleigh.name, libby.name, aiden.name, shep.name]
	y = [yeetus.population,carmen.population,david.population,jacey.population,ethan.population,sarah.population,kaleigh.population, libby.population, aiden.population, shep.population]

	plt.bar(x, y, color='yellow')
	plt.rcParams.update({'font.size': 35})
	plt.xlabel("Species'")
	plt.ylabel("population")
	plt.rcParams.update({'font.size': 35})
	plt.title("Natural selection simulator results (final)")

	plt.xticks(x, x)
	plt.savefig("final.png")
	plt.show()
